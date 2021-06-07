from django.shortcuts import render, get_object_or_404

from .models import ExpoPhotos, Expo


def expo(request):
    expos = Expo.objects.all()
    return render(request, 'expo/expo.html', {'expos': expos})


def expo_detail(request, id):
    expo = get_object_or_404(Expo, id=id)
    photos = ExpoPhotos.objects.filter(expo=expo)
    return render(request, 'expo/expo_detail.html', {
        'expo': expo,
        'photos': photos,
    })