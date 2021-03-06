from django.urls import path
from . import views

urlpatterns = [
    # we will define all app-level urls in this list
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('dogs/', views.dogs_index, name='index'),
    path('dogs/', views.DogIndex.as_view(), name='index'),
    path('dogs/<int:pk>/', views.dogs_detail, name='detail'),
    # path('dogs/<int:pk>/', views.DogDetail.as_view(), name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('toys/', views.ToyIndex.as_view(), name='toy_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name="toy_update"),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name="toy_delete"),
    path('dogs/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),
    # path('dogs/<int:pk>/delete_feeding/<int:feeding_id>', views.DeleteFeeding.as_view(), name='delete_feeding'),

    # associate a toy with a dog
    path('dogs/<int:pk>/assoc_toy/<int:fk>/', views.assoc_toy, name='assoc_toy'),
    # unassociate a toy with a dog
    path('dogs/<int:pk>/remove_assoc_toy/<int:fk>/', views.remove_assoc_toy, name='remove_assoc_toy'),
    # photo uploader
    path('dogs/<int:pk>/add_photo/', views.add_photo, name='add_photo'),
    # authentication sign up
    path('accounts/signup/', views.signup, name='signup'),
]
