from django.urls import path
from . import views

urlpatterns = [
    path('create_account/', views.create_account, name='Create Account'),
    path('save_ratings/', views.save_ratings, name='Save Ratings'),
]
