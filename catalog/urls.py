from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path('paintings/', views.painting_index, name="painting_index"),
    path('painting<int:pk>/', views.painting_detail, name="painting_detail"),
    path('painters/', views.painter_index, name="painter_index"),
    path('painter<int:pk>/', views.painter_detail, name="painter_detail"),
]

"""path('', views.index, name='index'),
    path('paintings/', views.PaintingListView.as_view(), name='paintings')"""