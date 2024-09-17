from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

class House(models.Model):
    #the shape of data
    #구체적으로 설명할수록 장고는 DB와 잘 소통한다.
    """Hosue Definition for Houses"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="Price", help_text="Positive Number Only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pet Allowed?",
        default=True, 
        help_text="Does  house allows pet?"
        )

    def __str__(self):
        return self.name

