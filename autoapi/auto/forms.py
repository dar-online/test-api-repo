from django.forms import ModelChoiceField, ModelForm
from .models import Order, Marka, Modell


class OrderForms(ModelForm):
    marka = ModelChoiceField(empty_label=None,
                                  queryset=Marka.object.all(),
                                  to_field_name="marka")
    model = ModelChoiceField(empty_label=None,
                                  queryset=Modell.object.all(),
                                  to_field_name="model")

    class Meta:
        model = Order
        fields = ['id', 'autor_name', 'marka', 'model', 'category', 'release', 'price']
