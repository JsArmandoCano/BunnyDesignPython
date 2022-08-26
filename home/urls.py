from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('home/', views.Home, name="home"),
    path('register-contact/', views.register_contact, name='register_contact'),
]