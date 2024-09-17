from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User) #User Model 관리
class CustomUserAdmin(UserAdmin):
    pass
