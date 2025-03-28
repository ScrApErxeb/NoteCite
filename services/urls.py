from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ServiceViewSet, ReviewViewSet


# Routing
router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/services/<int:service_id>/reviews/', ReviewViewSet.as_view({'get': 'list'}), name='service-reviews'),
    path('api/services/<int:service_id>/reviews/<int:review_id>/', ReviewViewSet.as_view({'get': 'retrieve'}), name='service-review-detail'),
]