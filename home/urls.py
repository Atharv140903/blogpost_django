from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('createpost/', createPost_view, name="createpost"),
    path('login/', login_view, name='login' ),
    path('logout-view/', logout_view, name="logout_view"),
    path('register/', register_view, name='register'),
    path('deletepost/<id>', deletePost_view, name="deletepost"),
    path('updatepost/<slug>/', updatePost_view, name="updatepost"),
]
