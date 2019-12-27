from rest_framework import serializers
from ..models import Order
from ..models import Marka
from ..models import Modell


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = ('id','marka')
        depth = 1


class ModellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modell
        fields = ('id','model')
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    marka_name = MarkaSerializer(source='marka', read_only=True)
    model_name = ModellSerializer(source='model', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'marka_name', 'model_name', 'release','category' ,'price']

