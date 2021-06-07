from django.contrib import admin

from .models import Expo, ExpoPhotos


class ExpoPhotosAdmin(admin.StackedInline):
    model = ExpoPhotos


@admin.register(Expo)
class ExpoAdmin(admin.ModelAdmin):
    inlines = [ExpoPhotosAdmin]

    class Meta:
        model = Expo


@admin.register(ExpoPhotos)
class ExpoPhotos(admin.ModelAdmin):
    pass