from django.db import models
from apps.products.models import PizzaVariantModel


DELIVERY_STATUS_CHOICES = (
    ('created', 'Created'),
    ('preparing', 'Preparing'),
    ('delivering', 'Delivering'),
    ('delivered', 'Delivered'),
)


class OrderModel(models.Model):
    customer_full_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_city = models.CharField(max_length=100)
    customer_post_code = models.CharField(max_length=50)
    delivery_status = models.CharField(choices=DELIVERY_STATUS_CHOICES,
        max_length=10, default='created')

    class Meta:
        db_table = 'order'


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, related_name='items', on_delete=models.DO_NOTHING)
    pizza_variant = models.ForeignKey(PizzaVariantModel, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'order_item'
