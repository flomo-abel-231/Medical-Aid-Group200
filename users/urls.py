from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(' ', views.home, name="home"),
    path("register/", views.register, name='register'),
    path("user_login/", views.user_login, name='user_login'),
    path("user_logout/", views.user_logout, name="user_logout")


]
