from rest_framework.routers import DefaultRouter
from apps.products.viewsets import PizzaViewSet
from apps.orders.viewsets import OrderViewSet

router = DefaultRouter()
router.register(r'pizzas', PizzaViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls
