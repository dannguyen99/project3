from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("menu", views.menu, name="menu"),
    path('signup', views.sign_up, name = 'sign_up'),
    path('signupview', views.signup_view, name = 'signup_view')
]
