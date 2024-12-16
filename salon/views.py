from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand, Cars

def index(request: WSGIRequest):
    return render(request, "index.html")

def add_data(request):
    bmw = Brand.objects.get_or_create(name="BMW", country="Germany", established_year=1916)[0]
    toyota = Brand.objects.get_or_create(name="Toyota", country="Japan", established_year=1937)[0]
    uzauto = Brand.objects.get_or_create(name="UzAutoMotors", country="Uzbekistan", established_year=1992)[0]

    Cars.objects.get_or_create(brand=bmw, model_name="X5", production_year=2023, price=60000.00, image='cars/https://www.istockphoto.com/photos/bmw')
    Cars.objects.get_or_create(brand=bmw, model_name="M3", production_year=2023, price=70000.00, image='cars/bmw_m3.jpg')
    Cars.objects.get_or_create(brand=toyota, model_name="Corolla", production_year=2023, price=20000.00, image='cars/toyota_corolla.jpg')
    Cars.objects.get_or_create(brand=toyota, model_name="Camry", production_year=2023, price=30000.00, image='cars/toyota_camry.jpg')
    Cars.objects.get_or_create(brand=uzauto, model_name="Cobalt", production_year=2023, price=15000.00, image='cars/cobalt.jpg')
    Cars.objects.get_or_create(brand=uzauto, model_name="Gentra", production_year=2023, price=17000.00, image='cars/gentra.jpg')

    return HttpResponse("Ma'lumotlar qo'shildi!")

def car_list(request):
    cars = Cars.objects.select_related('brand').all()
    return render(request, 'car_list.html', {'cars': cars})
