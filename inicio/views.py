from mimetypes import init
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from inicio.forms import CrearUsuario, UserUpdateForm, ProfileUpdateForm, BuscarUsuario
from django.contrib.auth.models import User
from django.contrib import messages
from reviews.models import Post


# Create your views here.

# Views para APP Inicio


def inicio(request):
    contexto = {}
    return render(request,'inicio.html', contexto)


# Recordar que para deslogearse se usa from django.contrib.auth.views import LogoutView directamente en la URL, y se usa como template view

# REGISTRARSE

def registrarse(request):
    if request.method == 'POST':
        registro_form = CrearUsuario(request.POST)
        
        if registro_form.is_valid():
            username = registro_form.cleaned_data['username'] 
            #Esto es solo para sumarlo al contexto.
            registro_form.save()
            return render(request,'inicio.html',{'registro_exitoso':f'Se creó el user {username}. Ya puedes iniciar sesion.'})
        else:
            return render(request, 'registro.html',{'registro_form':registro_form, 'msj':''})
    else:
        registro_form = CrearUsuario()
        return render(request, 'registro.html',{'registro_form':registro_form})

# INICIAR SESION

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    # Si el usuario ya está loggeado, nos lleva a inicio. En caso contrario, nos permite ir al formulario   

    else:
        if request.method == 'POST':
            login_form = AuthenticationForm(request, data=request.POST)
            # se almacena la información introducida por el usuario en el formulairo

            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                # Si la información en el formulario es valida, las almacena 
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('inicio')       

                else:
                    return render(request, 'login.html', {'login_form':login_form, 'msj':'No se autenticó.'})     
            else:
                return render(request, 'login.html', {'login_form':login_form, 'msj':'Datos con formato incorrecto'} )
        else:
            login_form = AuthenticationForm()
            return render(request,'login.html', {'login_form':login_form} )




# PERFIL DE OTROS USUARIOS

# @login_required
# def perfil(request, usuario):
#     usuario = User.objects.get(username=usuario)
#     if usuario.username == request.user.username:
#         redirect('miperfil')
#     else:    
#         context = {

#             'usuario': usuario,
#             'nombre': usuario.first_name,
#             'apellido':usuario.last_name,
#             'email':usuario.email,
#             'avatar':usuario.perfilusuario.imagen,
#             'bio': usuario.perfilusuario.bio,
#             }

    
#         return render(request, 'perfil.html', context)

@login_required
def perfil(request, usuario):
    encontrado = User.objects.filter(username=usuario).exists()

    if encontrado:    
        usuario = User.objects.get(username=usuario)
        posts = Post.objects.filter(author=usuario)

        if usuario.username == request.user.username:
  
            return redirect('miperfil')
        else:    
            context = {

                'usuario': usuario,
                'nombre': usuario.first_name,
                'apellido':usuario.last_name,
                'email':usuario.email,
                'avatar':usuario.perfilusuario.imagen,
                'bio': usuario.perfilusuario.bio,
                'posts':posts,
                }

        
            return render(request, 'perfil.html', context)
    else:
        return render(request, 'perfil_inexistente.html', {})



# PERFIL DE USUARIO LOGEADO 

@login_required
def miperfil(request):
    usuario = request.user
    posts = Post.objects.filter(author=usuario)
    context = {

        'usuario': usuario,
        'nombre': request.user.first_name,
        'apellido':request.user.last_name,
        'email':request.user.email,
        'avatar':request.user.perfilusuario.imagen,
        'bio':request.user.perfilusuario.bio,
        'posts':posts
        }

    
    return render(request, 'miperfil.html', context)



# PERFIL DE USUARIO

@login_required
def perfil_update(request):
  
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.perfilusuario)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')

            return redirect('miperfil')
        


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.perfilusuario)

        context = {
            'u_form':u_form,
            'p_form':p_form,
            'usuario':request.user
        }

    return render(request,'editar_usuario.html',context)


# Buscador de usuarios

def buscador_usuarios(request):
    buscador_form = BuscarUsuario()
    if request.method == 'POST':
        buscador_form = BuscarUsuario(request.POST)

        if buscador_form.is_valid():
            data = buscador_form.cleaned_data
            usuario_buscado = data['usuario']
            coincidencias = User.objects.filter(username__icontains=usuario_buscado)
            busqueda = True

            contexto = {
                'busqueda':busqueda,
                'usuario_buscado':usuario_buscado,
                'coincidencias':coincidencias,
                'busqueda':busqueda,
                'buscador_form':buscador_form,

            }
            return render(request,'buscar_usuario.html',contexto)
        else:
            return render(request, 'buscar_usuario.html', {} )

        
    else:
        buscador_form = BuscarUsuario()
        coincidencias = []
        busqueda = False
        contexto = {
            'buscador_form':buscador_form,
            'coincidencias':coincidencias,
            'busqueda':busqueda
        }

        return render(request, 'buscar_usuario.html', contexto)
