from django.shortcuts import render
from rest_framework import  viewsets, permissions
from .models import Service, Review
from .serializers import ServiceSerializer, ReviewSerializer

# Create your views here.
# Views
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]