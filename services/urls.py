from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ServiceViewSet, ReviewViewSet


# Routing
router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]