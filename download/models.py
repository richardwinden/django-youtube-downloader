from django.db import models


class Download(models.Model):
    progress = models.IntegerField(null=True)  # process in percentage
# Create your models here.
