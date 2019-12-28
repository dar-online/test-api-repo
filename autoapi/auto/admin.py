from django.contrib import admin
from auto.models import *

# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_filter = ('category',)


@admin.register(CarMarka)
class AdminCarMark(admin.ModelAdmin):
    list_display = ('id', 'car_marka')
    list_filter = ('car_marka',)


@admin.register(CarModel)
class AdminCarModel(admin.ModelAdmin):
    list_display = ('id', 'car_model')
    list_filter = ('car_model',)


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ('id', 'price', 'year', 'name', 'car_marka', 'car_model')
    list_filter = ('price', 'year', 'name')