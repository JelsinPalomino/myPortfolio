from django.db import models

# Create your models here.
class Proyectos(models.Model):
    foto        = models.CharField(max_length = 1000)
    title       = models.CharField(max_length = 100)
    description = models.TextField(max_length = 100)
    tags        = models.CharField(max_length = 100, default= '')
    url         = models.CharField(max_length = 1000, default = '')
