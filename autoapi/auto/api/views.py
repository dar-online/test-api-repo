from rest_framework import generics, viewsets
from ..models import Order, Marka
from .serializers import OrderSerializer, MarkaSerializer


class OrdertListView(generics.ListAPIView):
    queryset = Order.object.all()
    serializer_class = OrderSerializer

