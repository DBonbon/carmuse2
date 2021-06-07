from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns

def __str__(self):
    """String for representing the Model object."""
    return self.title

class Photo(models.Model):
    title = models.CharField(max_length=60, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
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

class Expo(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the expo")
    photo = models.ManyToManyField(Photo, help_text="Select a photo for this expo")
    # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    class Meta:
        ordering = ['title',]


    def get_absolute_url(self):
        """Returns the url to access a particular expo instance."""
        return reverse('expo_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title


