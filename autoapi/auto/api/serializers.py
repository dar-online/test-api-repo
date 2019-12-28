from rest_framework import serializers
from ..models import *


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMarka
        fields = ('id','car_marka')
        depth = 1


class ModellSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('id','car_model')
        depth = 1


class CarSerializer(serializers.ModelSerializer):
    marka_name = MarkaSerializer(source='car_marka', read_only=True)
    model_name = ModellSerializer(source='car_model', read_only=True)

    class Meta:
        model = Car
        fields = ['name', 'marka_name', 'model_name', 'year','car_cat' ,'price']

