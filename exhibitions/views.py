from django.shortcuts import render, get_object_or_404

from .models import ExpoPhotos, Expo


def expos_list(request):
    expos = Expo.objects.all()
    return render(request, 'expos_list.html', {'expos': expos})


def expos_detail(request, id):
    expo = get_object_or_404(Expo, id=id)
    expophotos = ExpoPhotos.objects.filter(expo=expo)
    return render(request, 'expos_detail.html', {
        'expo': expo,
        'expophotos': expophotos,
    })