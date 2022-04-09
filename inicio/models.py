from django.db import models
from django.conf import settings
# Podría traer el modelo User usando   settings.AUTH_USER_MODEL,
from django.contrib.auth.models import User


# Create your models here.

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', default='default.jpg')
    bio = models.TextField(default='Sin datos...')

    def __str__(self):
        return self.user.username
        