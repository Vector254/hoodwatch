from django.contrib import admin
from .models import Profile, NeighbourHood, Business

# Register your models here.
admin.site.Register(Profile)
admin.site.Register(NeighbourHood)
admin.site.Register(Business)