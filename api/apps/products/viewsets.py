from rest_framework import routers, serializers, viewsets
from apps.products.models import PizzaModel
from apps.products.serializers import PizzaSerializer


class PizzaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
