from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User) #User Model 관리
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Prodile", {
            "fields": ("username", "password", "name", "email", "is_host"),
            "classes" : ("wide",),

            },
            ),
            ("Permissions",     {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes" : ("collapse",),
            },),
            ("Important dates", {
                "fields": ("last_login", "date_joined"),
                "classes" : ("collapse",),
                },
                ),
    )
    #fields =("email", "password", "name")

    list_display = ("username", "email","name","is_host") #col of admin user list
    
