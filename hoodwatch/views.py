from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm, PostForm
from .models import NeighbourHood, Profile, Business, Contacts, Posts
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    hoods = NeighbourHood.objects.all()
    params ={
        'hoods':hoods,
    }
    return render(request, 'index.html', params)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration_form.html',{'form':form})

def profile(request):
    
    user= request.user
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
           user_form.save() 
           profile_form.save()
           messages.success(request, f'Profile info updated successfully!')
           return redirect('profile' )

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    params = {
        'user_form':user_form,
        'profile_form':profile_form,
        'user':user,
        
       
    }
   
    return render(request, 'profile.html', params)

def hoods(request):
    hoods = NeighbourHood.objects.all()
    params ={
        'hoods':hoods,
    }

    return render(request, 'hoods.html',params)

def join(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.hood = hood
    request.user.profile.save()
    return redirect('index')


def leave(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('hoods')

def my_hood(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(hood=hood)
    params={
        'hood':hood,
        'business':business,
    }
    return render(request,'my_hood.html',params )

def business(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(hood=hood)
    params={
        'hood':hood,
        'business':business,
    }
    return render(request,'business.html',params )

def contacts(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    contacts = Contacts.objects.filter(hood=hood)
    params={
        'hood':hood,
        'contacts':contacts,
    }
    return render(request,'contacts.html',params )

def announcements(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    posts = Posts.objects.filter(hood=hood)
    current_user = request.user
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            add=form.save(commit=False)
            add.author = request.user.profile
            add.hood = hood
            add.save()
            return redirect('announcements',hood.id)
    params={
        'hood':hood,
        'posts':posts,
        'form':form,
    }
    return render(request,'announcements.html',params )

def search_results(request):
    if request.method == 'GET':
        name = request.GET.get("query")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search.html', {'message': message})

