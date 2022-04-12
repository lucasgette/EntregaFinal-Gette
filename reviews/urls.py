from django.urls import path
from .views import PostViews, PostDetailView, other_users_post, other_users_post_detail,crear_post, borrar_review, editar_review


urlpatterns = [
    # path('reviews/',reviews, name='reviews'),
    path('reviews/',PostViews.as_view(), name='reviews'),
  
    path('reviews/<str:username>/',other_users_post, name='other_users_post'),
    path('reviews/<str:author>/<int:pk>/',other_users_post_detail, name='other_users_post_detail'),
    path('crear-post/',crear_post, name='crear_post'),
    path('borrar-reviews/<str:author>/<int:pk>',borrar_review, name='borrar_review'),
    path('editar-reviews/<str:author>/<int:pk>',editar_review, name='editar_review'),
  
]