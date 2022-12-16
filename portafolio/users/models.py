from django.db import models

# Create your models here.
class BdIp(models.Model):
    ip = models.CharField(max_length=200)