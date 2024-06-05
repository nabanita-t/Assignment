from django.contrib import admin
from apps.social_network import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.FriendRequest)
