from django.contrib.auth.models import AbstractUser
from django.db import models

# Modèle Utilisateur avec rôles
# Modèle Utilisateur avec rôles
class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'Utilisateur'),
        ('admin', 'Admin'),
        ('authority', 'Autorité')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Ajoute un related_name unique
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Ajoute un related_name unique
        blank=True
    )

