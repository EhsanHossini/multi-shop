from django.forms import ModelForm, TextInput, NumberInput, Textarea
from .models import Contact


class ContactForms(ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "number", "subject", "body")
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Your Name", "id": "name"}),
            "number": NumberInput(attrs={"class": "form-control", "placeholder": "Your Number", "id": "number"}),
            "subject": TextInput(attrs={"class": "form-control", "placeholder": "Subject", "id": "subject"}),
            "body": Textarea(attrs={"class": "form-control", "placeholder": "Message", "id": "message", "rows": 8}),
        }
