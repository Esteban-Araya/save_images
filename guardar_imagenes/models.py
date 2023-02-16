from django.db import models

# Create your models here.

class Imagenes(models.Model):
    name = models.CharField(max_length=20)
    imageEncodes = models.TextField()