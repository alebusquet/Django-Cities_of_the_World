from django.shortcuts import render
from django.http import HttpResponse
from .models import City
# Create your views here.

def index(request):
    cities = City.objects.all()             # que del modelo City traiga todos los objetos
    
    # renderizar la salida en un template. Entre llaves indico que al objeto 'cities' 
    # le paso todas las ciudades, que fueron cargadas en la linea de arriba.
    return render(request, 'cities.html', {'cities': cities})


# Funcion para retornar una ciudad especifica:
def get_city(request, id):                      # aparte del request, recibe el id de la ciudad
    city = City.objects.get(id=id)              # que del modelo City traiga el objeto correspondiente al id
    
    return render(request, 'city.html', {'city': city}) # ahora es una ciudad lo que recibe el objeto 'city'

