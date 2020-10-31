from django.contrib import admin
from .models import Profile, NeighbourHood, Business, Contacts, Posts

# Register your models here.
admin.site.register(Profile)
admin.site.register(NeighbourHood)
admin.site.register(Business)
admin.site.register(Contacts)
admin.site.register(Posts)