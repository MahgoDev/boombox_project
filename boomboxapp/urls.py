from django.urls import path
from . import views

urlpatterns = [
    path('create_account/', views.create_account, name='Create Account'),
    path('add_albums/', views.add_albums, name='Albums added'),
    path('add_ratings/', views.add_ratings, name='Ratings added'),
]
