from django.shortcuts import render, get_object_or_404
from .models import Order, Modell, Marka
from .forms import OrderForms


def order_create(request):
    if request.method =="POST":
        create = OrderForms(request.POST)

        if create.is_valid():
            post = create.save(commit=False)
            post.save()
    else:

        create = OrderForms(request.POST)
    return render(request, 'auto/order/create.html',{'create':create} )



# Create your views here.

def order_list(request):
    orders = Order.object.all()
    return render(request, 'auto/order/list.html', {'orders': orders})


def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return  render(request, 'auto/order/detail.html', {'order': order })

