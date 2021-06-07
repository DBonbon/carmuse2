from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns


class Expo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    photo = models.FileField(blank=True)

    def __str__(self):
        return self.title


class ExpoPhotos(models.Model):
    expo = models.ForeignKey(Expo, default=None, on_delete=models.CASCADE)
    summary = models.TextField(max_length=200, default='', blank=True)
    photos = models.FileField(upload_to='expophotos/')

    def __str__(self):
        return self.expo.title


# the Expo is the post class, the ExpoPhoto is the detailed


    #todo: create instances of exhibitions to
    # a. create gallery of exhibitions in the exhibitions page
    # b. allow USERs to adminster exhibitions



