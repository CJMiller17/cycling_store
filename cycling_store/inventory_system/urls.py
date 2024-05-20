from django.urls import path, include
from rest_framework import routers
from inventory_system.views import *

router = routers.DefaultRouter()

router.register(r'inventory', InventoryViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]