from django.urls import path
from . import views

urlpatterns = [
    path('tarjetas/', views.Tarjetas, name='tarjetas'),
    path('tarjetas/<str:category>/', views.Tarjetas, name='products_by_category_tarjeta'),
    path('tarjetas/<str:category>/<slug:slug>/', views.detail_tarjeta, name='detail_tarjeta'),
    
    path('manualidades/', views.Manualidad, name='manualidades'),
    path('manualidades/<str:category>/', views.Manualidad, name='products_by_category_manualidad'),
    path('manualidades/<str:category>/<slug:slug>/', views.detail_manu, name='detail_manu'),
    
    path('dibypin/', views.DibyPins, name='dibypin'),
    path('dibypin/<str:category>/', views.DibyPins, name='products_by_category_dibypins'),
    path('dibypin/<str:category>/<slug:slug>/', views.detail_pin, name='detail_dibypin'),
    
    path('tela/', views.Telas, name='tela'),
    path('tela/<str:category>/', views.Telas, name='products_by_category_tela'),
    path('tela/<str:category>/<slug:slug>/', views.detail_tela, name='detail_tela'),
    
    path('comentarios/', views.all_commits, name='all'),
]