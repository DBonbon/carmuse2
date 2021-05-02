from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from .models import Painter, Painting, Medium, Support, Category, Location, Tag
from django_admin_inline_paginator.admin import TabularInlinePaginated



'''General sections'''
admin.site.register(Medium)
admin.site.register(Support)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Tag)

'''Painter section'''

""" TabutlarInlinePaginated needs to be installed instead of TabularInline model, in order to
enable pagination in the inlines
check: https://pypi.org/project/django-admin-inline-paginator/
"""


class PaintingsAdminInline(TabularInlinePaginated):
    # fields = (...)
    per_page = 3
    model = Painting


class PainterResource(resources.ModelResource):
    class Meta:
        model = Painter


class PainterAdmin(ImportExportModelAdmin):
    resources_class = PainterResource
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death', 'image')
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death'), 'biography', 'image']
    inlines = (PaintingsAdminInline,)
    # inlines = [PaintingsInline]
    # list_per_page = 2


admin.site.register(Painter, PainterAdmin)


'''Painting section'''


class PaintingResource(resources.ModelResource):
    class Meta:
        model = Painting


class PaintingAdmin(ImportExportModelAdmin):
    resources_class = PaintingResource
    list_display = ('id', 'title', 'painter', 'category', 'medium', 'display_tag', 'motif',)
    list_filter = ('title', 'painter', 'category', 'medium', 'motif')
    # filedsets allow to section the detailed view.
    #  group them in a tuple within a list to display them horizontally.
    fieldsets = (
        (None, {
            'fields': [('title', 'painter', 'dimensions'), 'description', 'image']
        }),
        ('Meta', {
            'fields': [('location', 'motif', 'tag'), ('category', 'medium', 'support')]
        }),
        ('Hidden items', {
            'fields': [('signature', 'date'), 'remark']
        }),
    )


admin.site.register(Painting, PaintingAdmin)


class ViewAdmin(ImportExportModelAdmin):
    pass

    # todo Section Painter and Painting
    # todo Stats tab (not Google Analytics!) similar to the home page
    # todo create user types, i.e. SuperUser, view only, limited by Paintings etc'.
    #








'''to do list in the Admin View:
- create section, Admin (users, groups)
- main (Painting, painter), 
- Stats
- Meta

For the stats
create stat calss in model.py
with def like
def index(request):
    num_ouevres = Painting.objects.all().count
    num_categories = Category.objects.all().count
    num_paintings = Painting.objects.filter(tag__exact='painting')all().count
    num_study = Painting.objects.filter(tag__exact='study')all().count


'''



'''class PaintingResource(resources.ModelResource):
    painter = fields.Field(attribute='painter', widget=ForeignKeyWidget(Painter), column_name='Painter')
    name = fields.Field(attribute='name', column_name='Name')
    support = fields.Field(attribute='support', widget=ForeignKeyWidget(Support), column_name='support')
    category = fields.Field(attribute='category', widget=ForeignKeyWidget(Support), column_name='category')
    tag = fields.Field(attribute='tag', widget=ManyToManyWidget(Tag), column_name='tag')
    # image = models.FilePathField(path="/image", null=True, blank=True)
    description = fields.Field(attribute='description', column_name='description')
    # remark = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        model = Painting
        fields =('name','painter', 'first_name', 'support', 'category', 'tag', 'date_of_birth', 'date_of_death', 'biography')
        export_order = fields'''
