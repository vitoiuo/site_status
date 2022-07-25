from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from core.user_down_urls import check_down_urls
from .models import Site, SiteStatus
from .forms import SiteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .user_down_urls import check_down_urls
# Create your views here.

def index(request):
    return render(request, 'core/pages/index.html')

@login_required
def sites_list(request):
    sites_list = Site.objects.filter(user_id=request.user)
    down_urls = check_down_urls(sites=sites_list, user=request.user)

    paginator = Paginator(sites_list, 3)
    page = request.GET.get('page')
    sites = paginator.get_page(page)

    context = {
        'sites':sites, 
        'down_urls':down_urls,
    }
    return render(request,'core/pages/sites_list.html',context)

@login_required
def view_site(request, id):
    site = get_object_or_404(Site, pk=id)
    last_status_infos = SiteStatus.objects.values('site_id').annotate(max_pk=Max('pk')).filter(site_id=site)
    for last_status in last_status_infos:
        for key, value in last_status.items():
            if key == 'max_pk':
                last_status = value
    status = SiteStatus.objects.get(id=last_status)
    context = {
        'site':site,
        'status':status,
    }
    return render(request, 'core/pages/site-view.html', context)

@login_required
def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user_id = request.user
            site.save()
            messages.info(request, 'Site adicionado com sucesso.')
            return redirect('sites-list')
    else:
        form = SiteForm()
        context = {
            'form':form
        }
        return render(request, 'core/pages/sites-register.html', context)

@login_required
def edit_site(request, id):
    site = get_object_or_404(Site, pk=id)
    form = SiteForm(instance=site)

    if(request.method=='POST'):
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            site.save()
            return redirect('sites-list')
        else:
            context = {
                'form':form,
                'site':site,
            }
            return render(request, 'core/pages/sites-edit.html', context)
    else:
        context = {
                'form':form,
                'site':site,
            }
        return render(request, 'core/pages/sites-edit.html', context)

@login_required
def delete_site(request, id):
    site = get_object_or_404(Site, pk=id)
    site.delete()

    messages.info(request, 'Site deletado com sucesso.')
    return redirect('sites-list')


