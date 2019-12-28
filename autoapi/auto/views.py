from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse


from auto.models import *
from auto.forms import CarAddForm

# Create your views here.

def cars_list(request):

    car_list = Car.object.all()

    context = {
        'car_list': car_list,
    }

    return render(request, 'car_list.html', context)


def car_form(request):
    if request.method == 'POST':
        form = CarAddForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            price = form.cleaned_data['price']
            name = form.cleaned_data['name']
            car_marka = form.cleaned_data['car_marka']
            car_model = form.cleaned_data['car_model']

            cat = Category.object.all()
            car_category = ''
            for i in cat:
                if int(year) <= i.max_date and int(year) >= i.min_date:
                    car_category = i.category

            qwe = Car(
                year = year,price=price,name=name,car_cat=car_category,car_marka=car_marka,car_model=car_model
            )
            qwe.save()
            return render(request, 'thank_you.html')

    else:
        form = CarAddForm()
    return render(request, 'car_form_add.html', {'form': form})



