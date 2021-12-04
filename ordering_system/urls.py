from django.contrib import admin
from django.urls import path, include
from .views import (
    index,
    vendor_create,
    vendor_list,
    vendor_delete,
    vendor_edit,
    delivery_label_create,
    delivery_label_list,
    delivery_label_delete,
    delivery_label_edit,
)


urlpatterns = [
    path("", index),
    path("accounts/", include("django.contrib.auth.urls")),
    path("vendor/new/", vendor_create, name="create-vendor"),
    path("vendor/", vendor_list, name="list-vendors"),
    path("vendor/<int:id>/edit/", vendor_edit, name="edit-vendor"),
    path("vendor/<int:id>/delete/", vendor_delete, name="delete-vendor"),
    path("delivery_label/new/", delivery_label_create, name="create-delivery-label"),
    path("delivery_label/", delivery_label_list, name="list-delivery-labels"),
    path(
        "delivery_label/<int:id>/edit/", delivery_label_edit, name="edit-delivery-label"
    ),
    path(
        "delivery_label/<int:id>/delete/",
        delivery_label_delete,
        name="delete-delivery-label",
    ),
]
