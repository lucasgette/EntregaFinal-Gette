from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView

# ListView permite listar querySets en nuestra página
# DetailView permite ver los detalles de un registro
from reviews.models import Post, Comentarios
from django.contrib.auth.models import User
from reviews.forms import CrearPost
from inicio.forms import Confirm


# Create your views here.

# def reviews(request):
#     context = {}
#     return render(request,'reviews.html',context)


# Para ver los posts del usuario autenticado

class PostViews(ListView):
    model = Post
    template_name = 'reviews.html'


# Para ver el detalle de los posts del usuario autenticado

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

    


# Para ver los posts de otros usuarios (distinto al autenticado)

def other_users_post(request, username):
    usuario = User.objects.get(username=username)
    
    if usuario == request.user:
        redirect('reviews')
    else:
        posts = Post.objects.filter(author=usuario)
        context = {'usuario':usuario, 'posts':posts}

        return render(request, 'other_user_posts.html',context)


# Para ver el detalle de los posts de otros usuarios (distinto al autenticado)

def other_users_post_detail(request, author, pk):
    post = Post.objects.get(pk=pk)
    comentarios = Comentarios.objects.filter(post=post)
    context = {'post':post, 'comentarios':comentarios}
 
    return render(request, 'post_details.html',context)
    


# Para crear un post

def crear_post(request):

    if request.method == 'POST':
        form_post = CrearPost(request.POST)
        if form_post.is_valid():
            data = form_post.cleaned_data

            nuevo_post = Post(title=data['title'], author=request.user, body=data['body'],calificacion=data['calificacion']) 
            nuevo_post.save()
            form_post = CrearPost()
            return redirect('miperfil')
        else:
            return render(request, 'crear_post.html', {'form_post':form_post, 'msj':'Datos con formato incorrecto'} )            

    else:
        form_post = CrearPost()
        context = {
            'form_post':form_post
        }
        return render(request,'crear_post.html',context)


# Editar post

def editar_review(request,author, pk):
    if author == request.user.username:
        post = Post.objects.get(pk=pk)

        if request.method == 'POST':
            form_editar_post = CrearPost(request.POST)

            if form_editar_post.is_valid():
                data = form_editar_post.cleaned_data

                post.title = data['title']
                post.body = data['body']
                post.calificacion = data['calificacion']
                post.save()

                return redirect('miperfil')
        else:
            form_editar_post = CrearPost(initial={'title':post.title, 'body':post.body,'calificacion':post.calificacion})

            contexto = {
                'form':form_editar_post,
                'post':post
            }

            return render(request, 'editar_review.html', contexto)

    else:
        
        return render(request,'editar_review.html', {'msj':'No tienes permiso para editar esta review'})


# Borrar post 

def borrar_review(request, author, pk):

    if author == request.user.username:
        post_borrar = Post.objects.get(pk=pk)

        if request.method == 'POST':
            confirm = Confirm(request.POST)

            if confirm.is_valid():
                data = confirm.cleaned_data

                if data['confirmation'] == True:
                    post_borrar.delete()
                    return redirect('miperfil')

        confirm = Confirm()
        context = {'confirm':confirm, 'post_borrar':post_borrar}

        return render(request, 'borrar_post.html', context)
    else:
        return redirect('miperfil')