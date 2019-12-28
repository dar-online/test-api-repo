from rest_framework import generics, viewsets
from ..models import *
from .serializers import CarSerializer


class OrdertListView(generics.ListAPIView):
    queryset = Car.object.all()
    serializer_class = CarSerializer

