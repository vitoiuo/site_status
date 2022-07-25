from .models import SiteStatus, Site

def check_down_urls(sites, user):
    sites_list_by_edit = Site.objects.filter(user_id=user).order_by('-sitestatus__id')[:len(sites)] 
    last_checks = SiteStatus.objects.filter(site_id__user_id=user).order_by('-id')[:len(sites)]
    down_urls = [site for site, check in zip(sites_list_by_edit, last_checks) if check.is_active == False]

    return down_urls