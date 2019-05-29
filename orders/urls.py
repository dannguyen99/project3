from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path('signup', views.sign_up, name = 'sign_up'),
    path('signupview', views.signup_view, name = 'signup_view'),
    path('login', views.log_in, name = 'log_in'),
    path('logout', views.log_out, name = 'log_out'),
    path('cart', views.cart, name = 'cart'),
    path('about', views.about, name = 'about')
]
