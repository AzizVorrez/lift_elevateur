from django.shortcuts import render
from .models import *

def index_view(request):
    communes = Communes.objects.all()
    keywords = Keywords.objects.all()
    
    data = {
        'communes' : communes,
        'keywords' : keywords
    }
    return render(request, 'index.html', data)


def index_city_view(request, id):

    communes = Communes.objects.all()
    commune_actif = Communes.objects.get(id = id)
    cities = Cities.objects.filter(id_com_id = id).order_by('lib_city')
    keywords = Keywords.objects.all()

    data = {
        'cities' : cities,
        'communes' : communes,
        'commune_actif' : commune_actif,
        'keywords' : keywords
    }
    return render(request, 'index.html', data)

def index_city_actif_view(request, lib_city):

    communes = Communes.objects.all()
    city_actif = Cities.objects.get(lib_city = lib_city)
    keywords = Keywords.objects.all()

    
    data = {
        'communes' : communes,
        'city_actif' : city_actif,
        'keywords' : keywords,
    }
    return render(request, 'index.html', data)