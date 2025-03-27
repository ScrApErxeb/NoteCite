from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import User


# Modèle Service
class Service(models.Model):
    CATEGORY_CHOICES = [
        ('health', 'Santé'),
        ('education', 'Éducation'),
        ('transport', 'Transport'),
        ('other', 'Autre')
    ]
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Avis de {self.user.username} sur {self.service.name}"