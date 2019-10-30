from rest_framework import serializers
from apps.products.models import PizzaModel, PizzaVariantModel


class PizzaVariantSerializer(serializers.ModelSerializer):
    pizza = serializers.StringRelatedField()

    class Meta:
        model = PizzaVariantModel
        fields = ['id', 'pizza', 'size']


class PizzaSerializer(serializers.ModelSerializer):
    variants = PizzaVariantSerializer(many=True)

    class Meta:
        model = PizzaModel
        fields = ['id', 'name', 'variants']
