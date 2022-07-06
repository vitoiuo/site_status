from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def sites_list(request):
    #Fazer um objects.all de sites do usuario
    return None
