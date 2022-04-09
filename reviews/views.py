from re import template
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
# ListView permite listar querySets en nuestra página
# DetailView permite ver los detalles de un registro
from reviews.models import Post
from django.contrib.auth.models import User
from reviews.forms import CrearPost


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
    context = {'post':post}
    return render(request, 'other_users_post_detail.html',context)
    


# Para crear un post

def crear_post(request):

    if request.method == 'POST':
        form_post = CrearPost(request.POST)
        if form_post.is_valid():
            data = form_post.cleaned_data

            nuevo_post = Post(title=data['title'], author=request.user, body=data['body'],calificacion=data['calificacion']) 
            nuevo_post.save()
            form_post = CrearPost()
            return redirect('inicio')
        else:
            return render(request, 'crear_post.html', {'form_post':form_post, 'msj':'Datos con formato incorrecto'} )            

    else:
        form_post = CrearPost()
        context = {
            'form_post':form_post
        }
        return render(request,'crear_post.html',context)