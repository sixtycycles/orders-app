from django import forms
from .models import Item, Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ("user", "vendor", )

    def save(self, commit: bool = True) -> Order:
        order: Order = super().save(commit)
        order.save()
        return order


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("order",)

    def save(self, commit: bool = True) -> Item:
        item: Item = super().save(commit)
        item.save()
        return item
