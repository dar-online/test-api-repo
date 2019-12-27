from django.urls import path
from . import views

app_name = 'auto'

urlpatterns = [
    path('', views.order_list, name = 'order_list'),
    path('<int:id>/', views.order_detail, name = 'order_detail'),
    path('create/', views.order_create, name= 'order_create'),
]