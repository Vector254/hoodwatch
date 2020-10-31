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
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=500)
    contact_info = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} NeighbourHood'

class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return f'{self.name} Business'
   