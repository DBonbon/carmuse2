from django.contrib import admin
from .models import ExpoPhotos, Expo


class ExpoPhotosAdmin(admin.StackedInline):
    model = ExpoPhotos


@admin.register(Expo)
class ExpoAdmin(admin.ModelAdmin):
    inlines = [ExpoPhotosAdmin]

    class Meta:
        model = Expo


@admin.register(ExpoPhotos)
class ExpoPhotosAdmin(admin.ModelAdmin):
    pass

