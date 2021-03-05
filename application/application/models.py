from django.db import models
from django.utils import timezone


class AbstractBaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
