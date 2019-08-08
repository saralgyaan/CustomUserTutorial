from django.shortcuts import render

# Create your views here.
# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import MyUserCreationForm


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
