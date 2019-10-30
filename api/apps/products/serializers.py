from rest_framework import serializers
from apps.products.models import PizzaModel, PizzaVariantModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ['name']


class PizzaVariantSerializer(serializers.ModelSerializer):
    pizza = serializers.StringRelatedField()

    class Meta:
        model = PizzaVariantModel
        fields = ['pizza', 'size']
