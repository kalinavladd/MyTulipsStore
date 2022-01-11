from .service import send

from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForms


class ContactView(CreateView):
    model = Contact
    form_class = ContactForms
    success_url = "/"

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)  # далее SMTP настраиваем в settings