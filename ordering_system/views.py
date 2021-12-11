import json
from typing import Any, Dict, List, cast
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, render,redirect

from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from .forms import ItemForm, OrderCreateForm
from .models import Item, Order


def landing_page(request):
    return render(request, 'ordering_system/landing.html')


def order_list_view(request):
    context = {}
    context["object_list"] = Order.objects.all()
    context["form"] = OrderCreateForm()

    return render(request, "ordering_system/order_list.html", context)


def order_create_view(request):
    context = {}
    form = OrderCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            order = form.save()

            return redirect(f"/orders/{order.pk}/")

    context["form"] = form
    return render(request, "ordering_system/order_create_form.html", context)


def order_detail_view(request, pk):
    context = {}
    context["order"] = get_object_or_404(Order, pk=pk)

    return render(request, "ordering_system/order_detail.html", context)


def order_add_item_view(request, pk):
    context = {}
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        cast(Order, order.items.create())

    context["Order"] = Order
    return render(request, "ordering_system/order_items.html", context)


def order_delete_view(request, pk):
    context = {}
    obj = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        obj.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def item_create_view(request, pk):
    context = {}
    order = get_object_or_404(Order, pk=pk)

    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.order = order
            form.save()
            return HttpResponseRedirect(
                reverse("item-detail", kwargs={"pk": form.instance.pk})
            )

    context["form"] = form
    context["order_id"] = pk
    return render(request, "ordering_system/item_create_form.html", context)


def item_edit_view(request, pk):
    context = {}
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=item)

    # save the data from the form and redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("item-detail", kwargs={"pk": item.pk}))

    context["form"] = form
    return render(request, "ordering_system/item_edit_form.html", context)


def item_detail_view(request, pk):
    context = {}
    item = get_object_or_404(Item, pk=pk)
    context["item"] = item

    return render(request, "ordering_system/item_detail.html", context)


def item_delete_view(request, pk):
    context = {}
    obj = get_object_or_404(Item, pk=pk)

    if request.method == "POST":
        obj.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
