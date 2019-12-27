from django.contrib import admin
from .models import Marka, Modell, Order


# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('autor_name', 'marka', 'model', 'category', 'release', 'price')
    list_filter = ('autor_name', 'marka', 'model', 'category', 'release', 'price')
    date_hierarchy = 'release'
    ordering = ('category', 'release')

@admin.register(Marka)
class MarkaAdmin(admin.ModelAdmin):
    list_display = ('marka',)

@admin.register(Modell)
class ModellAdmin(admin.ModelAdmin):
    list_display = ('model',)