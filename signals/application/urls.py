from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create-post/', views.create_post, name='create_post'),
    path('delete-post/<int:pk>/', views.delete_post, name='delete_post'),
]
