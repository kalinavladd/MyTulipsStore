from django import forms
from .models import Contact


class ContactForms(forms.ModelForm):
    """Форма подписки"""
    class Meta:
        model = Contact
        fields = ("name", "contact", "email", "text")

        widgets = {
            "name": forms.TextInput(attrs={"class": "footer__input", "placeholder": "Введите Ваше имя"}),
            "contact": forms.TextInput(attrs={"class": "footer__input", "placeholder": "Ваш контактный номер телефона"}),
            "email": forms.TextInput(attrs={"class": "footer__input", "placeholder": "Email"}),
            "text": forms.TextInput(attrs={"class": "footer__input footer__input-text", "placeholder": "Введите текст"})
        }

        labels = {
            "name": "",
            "contact": "",
            "email": "",
            "text": "",
        }
