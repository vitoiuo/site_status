from django.db import models
from django.conf import settings
# Create your model here.

class Site(models.Model):
    url = models.URLField(max_length=512)
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name