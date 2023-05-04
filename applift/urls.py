from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name = 'accueil'),
    path('<int:id>/', views.index_city_view, name = 'accueil-com'),
    path('<str:lib_city>/', views.index_city_actif_view, name='accueil-city')
]