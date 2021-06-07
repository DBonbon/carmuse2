from django.shortcuts import render

from .models import Photo, Expo
from django.views import generic


def photo_carousel(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, 'exhibitions/carousel.html', context)


class ExpoListView(generic.ListView):
    """Generic class-based list view for a list of expositions."""
    model = Expo
    expos = Expo.objects.all()
    paginate_by = 10


class ExpoDetailView(generic.DetailView):
    """Generic class-based detail view for an expo."""
    model = Expo

    def expo_carousel(request):
        queryset = Expo.objects.all()
        context = {
            "photos": queryset,
        }
        return render(request, 'exhibitions/carousel.html', context)


