from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    # path('', views.photo_carousel, name='exhibitions'),
    # path('expo/<int:pk>', views.BookDetailView.as_view(), name='expo_detail'),
    path('', views.expo, name='expo'),
    path('<int:id>/', views.expo_detail, name='expo_detail')
    ]

