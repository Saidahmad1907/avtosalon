from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Brand, Cars

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'established_year')

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'production_year', 'price')
    list_filter = ('brand', 'production_year')
    search_fields = ('model_name',)

