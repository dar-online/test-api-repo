from django.urls import path
from . import views

app_name = 'auto'

urlpatterns = [
    path('', views.OrdertListView.as_view(), name='order_list'),

]