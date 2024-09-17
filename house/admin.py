from django.contrib import admin
from .models import House

@admin.register(House) 
class HouseAdmin(admin.ModelAdmin):
    #이 클래스가 admin하게될 model은 House이다.
    fields = (
        "name",
        "address",
        "price_per_night",
        "pets_allowed",
        #("price","pets_allowed"), #same row
    )
    list_display = (
        "name",
        "price_per_night",
        "address",
        "pets_allowed"
    )
    list_filter = ("price_per_night", "pets_allowed")
    search_fields = ("address__startswith",)#(e1,)
    list_display_links = ("name", "address")
    list_editable = ("pets_allowed",)
 