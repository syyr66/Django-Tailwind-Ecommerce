from django import forms 

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "email", "address"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "w-[18rem] border border-gray-300 focus:border-white focus:ring focus:ring-indigo-200 outline-none px-4 py-2 rounded-md"}),
            "email": forms.TextInput(attrs={"class": "w-[18rem] border border-gray-300 focus:border-white focus:ring focus:ring-indigo-200 outline-none px-4 py-2 rounded-md"}),
            "address": forms.TextInput(attrs={"class": "w-[18rem] border border-gray-300 focus:border-white focus:ring focus:ring-indigo-200 outline-none px-4 py-2 rounded-md"}),
        }