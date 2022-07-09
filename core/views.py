from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Site
# Create your views here.

def index(request):
    return render(request, 'core/pages/index.html')

def sites_list(request):
    #PAGINAÇÃO - EM PROGRESSO
    sites = Site.objects.all()

    return render(request,'core/pages/sites_list.html',{'sites':sites})
