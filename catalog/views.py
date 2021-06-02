from django.shortcuts import render
from . models import Painter, Painting, Category, Support
# from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    num_ouevres = Painting.objects.all().count
    # num_painters = Painter.objects.all().count
    num_categories = Category.objects.all().count
    num_supports = Support.objects.all().count

    num_authors = Painter.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_ouevres': num_ouevres,
        'num_categories': num_categories,
        # 'num_painters': num_painters,
        'num_supports': num_supports,
        'num_visits': num_visits,
    }

    return render(request, 'catalog/index.html', context)


def painting_index(request):
    paintings = Painting.objects.all()
    paginator = Paginator(paintings, 24)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, "catalog/painting_index.html", context)

"""
def search(request):
    if request.method == "POST":
        search = request.POST['search']
        paintings = Painting.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))

        context = {
                'search': search,
                'paintings': paintings,

        }

        return render(request, "catalog/art_search.html", context)
"""


def art_search(request):
        if request.method=="GET":
            query=request.GET.get('q')
            paintings=Painting.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

        context = {
            'query': query,
            'paintings': paintings,
        }

        return render(request, "catalog/art_search.html", context)


def painting_detail(request, pk):
    painting = Painting.objects.get(pk=pk).count
    context = {"painting": painting}
    return render(request, "catalog/painting_detail.html", context)


def painter_index(request):
    painters = Painter.objects.all()
    # paginator = Paginator(painters, 6)

    # age_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    # context = {'page_obj': page_obj}
    context = {'painters': painters}
    return render(request, "catalog/painter_index.html", context)


def painter_detail(request, pk):
    painter = Painter.objects.get(pk=pk).count
    context = {"painter": painter}
    return render(request, "catalog/painter_detail.html", context)


