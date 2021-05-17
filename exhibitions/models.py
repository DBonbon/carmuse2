from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=60, default='', blank=True)
    description = models.TextField(default='', blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(width_field="width", height_field="height")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["timestamp"]
        verbose_name = 'Photo'

    #todo: create instances of exhibitions to
    # a. create gallery of exhibitions in the exhibitions page
    # b. allow USERs to adminster exhibitions

