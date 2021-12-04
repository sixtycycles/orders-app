from django.shortcuts import get_object_or_404, render, redirect
from .models import Order, OrderRequirements
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import VendorForm, DeliveryLabelForm
from .models import Vendor, DeliveryLabel


def index(request):
    context = {}
    return render(request, "landing.html", context)


###########################################################
# the views in this file are organized per entity and are #
# defined in C.R.U.D. order, Create, Read, Update, Delete #
###########################################################


def vendor_create(request):

    template = "vendor_create.html"
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/vendor/")
    context = {"form": form}
    return render(request, template, context)


def vendor_list(request):
    template = "vendor_list.html"
    list_of_vendors = Vendor.objects.all()
    context = {"list_of_vendors": list_of_vendors}

    return render(request, template, context)


def vendor_edit(request, id):

    template = "vendor_update.html"
    vendor = get_object_or_404(Vendor, id=id)
    form = VendorForm(request.POST or None, instance=vendor)

    if form.is_valid():
        vendor.name = form.cleaned_data["name"]
        vendor.street = form.cleaned_data["street"]
        vendor.city = form.cleaned_data["city"]
        vendor.state = form.cleaned_data["state"]
        vendor.zip = form.cleaned_data["zip"]
        vendor.phone = form.cleaned_data["phone"]
        vendor.save()
        redirect("/vendor/")

    context = {"form": form, "vendor": vendor}
    return render(request, template, context)


def vendor_delete(request, id):
    context = {}
    template = "vendor_delete.html"
    obj = get_object_or_404(Vendor, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("/vendor/")

    return render(request, template, context)


########################
# Delivery Label Views #
########################


def delivery_label_create(request):

    template = "delivery_label_create.html"
    form = DeliveryLabelForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("/delivery_label/")

    context = {"form": form}

    return render(request, template, context)


def delivery_label_list(request):
    template = "delivery_label_list.html"
    list_of_delivery_labels = DeliveryLabel.objects.all()
    context = {"list_of_delivery_labels": list_of_delivery_labels}

    return render(request, template, context)


def delivery_label_edit(request, id):

    template = "delivery_label_update.html"
    delivery_label = get_object_or_404(DeliveryLabel, id=id)
    form = DeliveryLabelForm(request.POST or None, instance=delivery_label)

    if form.is_valid():
        delivery_label.name = form.cleaned_data["name"]
        delivery_label.street = form.cleaned_data["street"]
        delivery_label.city = form.cleaned_data["city"]
        delivery_label.state = form.cleaned_data["state"]
        delivery_label.zip = form.cleaned_data["zip"]
        delivery_label.phone = form.cleaned_data["phone"]
        delivery_label.save()
        redirect("/delivery_label/")

    context = {"form": form, "delivery_label": delivery_label}

    return render(request, template, context)


def delivery_label_delete(request, id):
    context = {}
    template = "delivery_label_delete.html"
    obj = get_object_or_404(DeliveryLabel, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("/delivery_label/")

    return render(request, template, context)


########################
# Order Item Views #
########################
