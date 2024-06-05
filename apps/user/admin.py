from django.contrib import admin
from apps.user import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.UserSessionInfo)
