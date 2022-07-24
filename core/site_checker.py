from core.models import Site, SiteStatus
from urllib.error import HTTPError
import urllib.request

def sites_checker():
        sites = Site.objects.values('url')
        for site in sites:
            for search_url in site.values():
                site_under_view = Site.objects.get(url=search_url)
                try:
                    status = urllib.request.urlopen(search_url).getcode()
                except HTTPError as erro:
                    SiteStatus.objects.create(request_code=erro.code, site_id=site_under_view)
                else:
                    SiteStatus.objects.create(request_code=status, site_id=site_under_view)
                    