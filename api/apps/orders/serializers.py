from rest_framework import serializers
from apps.orders.models import OrderModel, OrderItemModel, DELIVERY_STATUSES
from apps.products.models import PizzaVariantModel
from apps.products.serializers import PizzaVariantSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    pizza_variant = PizzaVariantSerializer(read_only=True)
    pizza_variant_id = serializers.PrimaryKeyRelatedField(
        queryset=PizzaVariantModel.objects.all(), write_only=True)

    class Meta:
        model = OrderItemModel
        fields = ['id', 'pizza_variant', 'pizza_variant_id', 'quantity']


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

    def validate_delivery_status(self, value):
        if not self.instance and value != DELIVERY_STATUSES[0][0]:
            raise serializers.ValidationError('Invalid value for first delivery status')
        elif self.instance and value != self.instance.delivery_status:
            delivery_statues_keys = list(zip(*DELIVERY_STATUSES))[0]
            if delivery_statues_keys.index(value) < delivery_statues_keys.index(self.instance.delivery_status):
                raise serializers.ValidationError('Invalid value for next delivery status')
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = OrderModel.objects.create(**validated_data)
        for item_data in items_data:
            item_data['pizza_variant'] = item_data.pop('pizza_variant_id')
            OrderItemModel.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', [])
        for item_data in items_data:
            item_data['pizza_variant'] = item_data.pop('pizza_variant_id')
            if 'id' in item_data:
                obj_order_item = OrderItemModel.objects\
                    .filter(order=instance, pk=item_data['id'])\
                    .update(**item_data)
            else:
                OrderItemModel.objects.create(order=instance, **item_data)
        return super(OrderSerializer, self).update(instance, validated_data)
