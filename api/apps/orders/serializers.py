from rest_framework import serializers
from apps.orders.models import OrderModel, OrderItemModel
from apps.products.models import PizzaVariantModel
from apps.products.serializers import PizzaVariantSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    pizza_variant = PizzaVariantSerializer(read_only=True)
    pizza_variant_id = serializers.PrimaryKeyRelatedField(
        queryset=PizzaVariantModel.objects.all(), write_only=True)

    class Meta:
        model = OrderItemModel
        fields = ['id', 'pizza_variant', 'pizza_variant_id']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = OrderModel
        fields = [
            'id',
            'customer_full_name',
            'customer_address',
            'customer_city',
            'customer_post_code',
            'delivery_status',
            'items'
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = OrderModel.objects.create(**validated_data)
        for item_data in items_data:
            item_data['pizza_variant'] = item_data.pop('pizza_variant_id')
            OrderItemModel.objects.create(order=order, **item_data)
        return order
