from django.urls import path
from .views import PostViews, PostDetailView, other_users_post, other_users_post_detail,crear_post

urlpatterns = [
    # path('reviews/',reviews, name='reviews'),
    path('reviews/',PostViews.as_view(), name='reviews'),
    path('review/<int:pk>',PostDetailView.as_view(), name='review_detail'),
    path('reviews/<str:username>/',other_users_post, name='other_users_post'),
    path('reviews/<str:author>/<int:pk>/',other_users_post_detail, name='other_users_post_detail'),
    path('crear-post/',crear_post, name='crear_post')


]