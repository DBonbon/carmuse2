from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Picture(models.Model):
    Tittle = models.CharField(max_length=100, null=True, blank=True)
    image = CloudinaryField('image')