from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from .models import NeighbourHood, Profile, Business

# Create your views here.

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