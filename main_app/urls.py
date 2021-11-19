from django.urls.resolvers import URLPattern


from django.urls import path
from . import views

urlpatterns = [
    # we will define all app-level urls in this list
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('dogs/', views.dogs_index, name='index'),
    path('dogs/', views.DogIndex.as_view(), name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
]
