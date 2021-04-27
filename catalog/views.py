from django.shortcuts import render
from catalog.models import Painter, Painting, Category, Support
from django.views import generic


def index(request):
    num_ouevres = Painting.objects.all().count
    num_painters = Painter.objects.all().count
    num_categories = Category.objects.all().count
    num_supports = Support.objects.all().count

    num_authors = Painter.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_ouevres': num_ouevres,
        'num_categories': num_categories,
        'num_painters': num_painters,
        'num_supports': num_supports,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


def painting_index(request):
    paintings = Painting.objects.all()
    context = {"paintings": paintings}
    return render(request, "painting_index.html", context=context)


def painting_detail(request, pk):
    project = Painting.objects.get(pk=pk)
    context = {"painting": project}
    return render(request, "painting_detail.html", context=context)


def painter_index(request):
    painters = Painter.objects.all()
    context = {"painters": painters}
    return render(request, "painter_index.html", context=context)


def painter_detail(request, pk):
    painter = Painter.objects.get(pk=pk)
    context = {"painter": painter}
    return render(request, "painter_detail.html", context=context)


# class BookListView(generic.ListView):
#    model = Painting