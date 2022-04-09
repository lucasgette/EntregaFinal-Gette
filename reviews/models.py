from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    calificacion = models.FloatField(
        validators=[MinValueValidator(0.0), 
                    MaxValueValidator(10.0)])

    def __str__(self):
        return self.title + ' | ' + str(self.calificacion) + ' | ' + self.author.username