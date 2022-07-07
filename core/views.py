from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Site
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def sites_list(request):
    #PAGINAÇÃO - EM PROGRESSO
    sites_list = Site.objects.filter(user_id=1)
    paginator = Paginator(sites_list, 3)
    page = request.GET.get('page')
    sites = paginator.get_page(page)

    return render(request,'core/sites_list.html',{'sites':sites})
