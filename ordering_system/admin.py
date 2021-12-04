from django.contrib import admin
from .models import Vendor, DeliveryLabel


# Register your models here.
@admin.register(
    Vendor,
)
class VendorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "city",
        "state",
        "zip",
    ]

    list_filter = [
        "city",
        "state",
        "zip",
    ]


@admin.register(DeliveryLabel)
class DeliveryLabel(admin.ModelAdmin):
    ...
