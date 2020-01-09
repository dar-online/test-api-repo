from django.shortcuts import render

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
            post = form.save(commit=False)
            post.save()
            return render(request, 'add_complete.html')
    else:
        form = CarAddForm()
    return render(request, 'car_form_add.html', {'form': form})
