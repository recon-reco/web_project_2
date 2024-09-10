from django.db import models


class House(models.Model):
    #the shape of data
    #구체적으로 설명할수록 장고는 DB와 잘 소통한다.
    """Hosue Definition for Houses"""
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    

