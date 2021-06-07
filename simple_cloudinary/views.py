from django.shortcuts import render
from .models import Picture

def index_cloudinary(request):
    picutres = Picture.objects.all()
    context = {'picutres': picutres}
    return render(request, 'picutres.html', context)