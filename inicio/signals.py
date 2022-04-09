from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PerfilUsuario


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)

# Sender: User
# Signal: post_save
# create_profile: es el receiver, que con todos los argumentos hará una tarea

# instance -> Es la instancia del usuario que fue creado


# Ahora podemos crear una función que permite guardar el perfil
# cuando el usuario es guardado.

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.perfilusuario.save()


# Recordar importar las señales dentro de la función ready() en userconfig de apps.py