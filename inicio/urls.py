from django.contrib import admin
from django.urls import path
from inicio.views import inicio, login_usuario, perfil, registrarse,perfil,perfil_update, miperfil, buscador_usuarios, buscador_reviews

from django.contrib.auth.views import LogoutView


#URLs para INICIO

urlpatterns = [
 
    path('',inicio, name='inicio'),
    path('login/',login_usuario, name='login'),
    path('perfil/',perfil, name='perfil'),

    #Para logout se usa LogoutView
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registrarse/',registrarse, name='registrarse'),
    path('perfil/<str:usuario>/',perfil, name='perfil'),
    path('miperfil/',miperfil, name='miperfil'),
    path('perfil/editar',perfil_update, name='editar_perfil'),
    path('buscar-usuarios/',buscador_usuarios, name='buscar_usuario'),
    path('buscar-reviews/',buscador_reviews, name='buscar_reviews'),

    
    
    

    
]
