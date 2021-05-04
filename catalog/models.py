from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Medium(models.Model):
    """Model representing he type of art material used (e.g. watercolor, oil, etc')."""
    name = models.CharField(
        max_length=205,
        help_text="Enter a medium used to paint (e.g. ink, acrylic etc.)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Support(models.Model):
    """Model representing the surface on which a painting is made: canvas, paper')."""
    name = models.CharField(
        max_length=200,
        help_text="Enter the painting's surface (e.g. canvas, wood etc.)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Category(models.Model):
    """Model representing the painting's category (e.g. Painting, Drawing, etc')."""
    name = models.CharField(
        max_length=200,
        help_text="Enter the painting's category (e.g. Sketch, Study, Drawing, Painting, etc.)"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Tag(models.Model):
    """Model representing the the mise-en-scene category (e.g. portrait, landscape, etc')."""
    name = models.CharField(
        max_length=200,
        help_text="Enter the painting's tags (e.g. boats, family, mountains, etc.)"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Location(models.Model):
    """Model representing the region, city where the painting was made."""
    name = models.CharField(
        max_length=200,
        help_text="Enter the painting's category (e.g. Genève, Alger, etc.)"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Painting(models.Model):
    '''Model representing a painting'''
    title = models.CharField(max_length=200)
    painter = models.ForeignKey('Painter', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because a painting can have only one painter, but a painter can paint multiple paintings
    # Painter as a string rather than object because it hasn't been declared yet in the file
    description = models.TextField(max_length=1000, blank=True, help_text='Enter a brief description of the Painting')
    MOTIF_TYPES = (
        ('ge', 'Genre painting (everyday life)'),
        ('por', 'Portrait'),
        ('apa', 'Autoportrait'),
        ('la', 'Landscape'),
        ('nm', 'Still life'),
        ('ot', 'Other'),
    )
    motif = models.CharField(
        max_length=3,
        choices=MOTIF_TYPES,
        blank=True,
        # default='ot',
        help_text='The subject-matter')
    medium = models.ForeignKey(Medium, on_delete=models.SET_NULL, blank=True, null=True)
    support = models.ForeignKey(Support, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True, help_text="Select tags for this painting")
    image = models.ImageField(null=True, blank=True) # , upload_to='paintings'
    # image = models.ImageField(path="catalog\\static\\images\\", null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    dimensions = models.CharField(max_length=20, null=True, blank=True)
    signature = models.BooleanField(null=True, blank=True)
    remark = models.TextField(max_length=200, null=True, blank=True, help_text="Enter any remark that doesn't match any other category")

    class Meta:
        ordering = ['title', 'painter']

    def display_tag(self):
        """Creates a string for the Tags. This is required to display tags in Admin."""
        return ', '.join([tag.name for tag in self.tag.all()[:3]])

    display_tag.short_description = 'Tag'

    '''def get_absolute_url(self):
        """#Returns the url to access a particular painting instance."""
        #return reverse('paint-detail', arg=[str(self.id)])'''

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Painter(models.Model):
    """Model representing a painter."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)
    image = models.ImageField(null=True, blank=True) # , upload_to="painters"
    biography = models.TextField(null=True, blank=True, help_text="Describe painter's biography")
    remark = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    '''def get_absolute_url(self):
        """Returns the url to access a particular painter instance."""
        return reverse('painter-detail', args=[str(self.id)])'''

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

