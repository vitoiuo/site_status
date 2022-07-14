from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UsuarioForm

class SignUp(generic.CreateView):
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
