
from django.conf.urls import url, include
from django.urls import path
from users.views import dashboard


urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    # path('', dashboard, name="dashboard"),
]