from django.urls import path
from .views import index, add_data, car_list

urlpatterns = [
    path('', index, name='index'),
    path('add-data/', add_data, name='add_data'),
    path('cars/', car_list, name='car_list'),
]

