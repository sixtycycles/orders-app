from django import forms
from .models import Vendor, DeliveryLabel
from localflavor.us.forms import USPSSelect, USStateSelect

# class CreateNewOrderForm(forms.Form):
#     prefix = 'create_order_form'
#     your_name = forms.CharField(label='Your name', max_length=100)


class VendorForm(forms.ModelForm):
    name = forms.TextInput()
    street = forms.TextInput()
    city = forms.TextInput()
    # state = USStateSelect()
    class Meta:
        model = Vendor
        fields = ["name", "street", "city", "state", "zip", "phone"]


class DeliveryLabelForm(forms.ModelForm):

    mark_urgent = forms.BooleanField(widget=forms.CheckboxInput())

    # state = USStateSelect()
    class Meta:
        model = DeliveryLabel
        fields = [
            "deliver_to",
            "email",
            "room_number",
            "ship_method",
            "delivery_date",
            "mark_urgent",
            "order_contact_name",
            "order_contact_email",
            "order_contact_phone",
        ]
