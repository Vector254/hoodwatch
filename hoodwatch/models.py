from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    hood = models.ForeignKey('NeighbourHood', on_delete=models.CASCADE,related_name='occupants', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return f'{self.name} NeighbourHood'

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def search_hood(cls, name):
        return cls.objects.filter(name__icontains=name).all()

class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    hood = models.ForeignKey(NeighbourHood,related_name='business', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return f'{self.name} Business'

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

   
class Contacts(models.Model):
    hood = models.ForeignKey(NeighbourHood,related_name='contacts', on_delete=models.CASCADE)
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.hood} Contacts'


class Posts(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField(blank=True, max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author')
    hood = models.ForeignKey(NeighbourHood,related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.hood} Posts'
