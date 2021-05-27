
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path, include
# from users.views dashboard
from users import views as user_views

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    path('profile/', user_views.profile, name='profile'),
    # url(r"^dashboard/", dashboard, name="dashboard"),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # url(r"^register/", register, name="register"),
    # path('', dashboard, name="dashboard"),
]