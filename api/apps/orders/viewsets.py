from rest_framework import routers, serializers, viewsets
from apps.orders.models import OrderModel
from apps.orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.filter(deleted_at=None)
    filterset_fields = [
        'customer_full_name',
        'customer_address',
        'customer_city',
        'customer_post_code',
        'delivery_status'
    ]
