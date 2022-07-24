from http import HTTPStatus
from django.db import models
from django.conf import settings
# Create your model here.

class Site(models.Model):
    url = models.URLField(max_length=512)
    name = models.CharField(max_length=128)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

class SiteStatus(models.Model):
    request_code = models.CharField(max_length=16)
    is_active = models.BooleanField(default=False)
    last_check = models.DateTimeField(auto_now_add=True)
    site_id = models.ForeignKey('Site', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.request_code == HTTPStatus.OK:
            self.is_active=True
        super(SiteStatus, self).save(*args, **kwargs)

