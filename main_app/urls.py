from django.urls import path
from . import views

urlpatterns = [
    # we will define all app-level urls in this list
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('dogs/', views.dogs_index, name='index'),
    path('dogs/', views.DogIndex.as_view(), name='index'),
    # path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
]
