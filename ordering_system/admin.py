from django.contrib import admin

from .models import Item, Order,Vendor

# Register your models here.
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Vendor)
