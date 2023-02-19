from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ContactForm
from .models import Contact


class ContactCreateView(CreateView):
    form_class = ContactForm
    model = Contact
    queryset = Contact.objects.all()
    success_url = "/"



