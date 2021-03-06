from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse
from .models import Dog, Toy, Photo
from .forms import FeedingForm

import boto3
import uuid

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'dogcollector-photo-uploads'



# Add the Cat class & list and view function below the imports
# class Dog:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, gender, description, age):
#     self.name = name
#     self.breed = breed
#     self.gender = gender
#     self.description = description
#     self.age = age

# dogs = [
#   Dog('Lolo', 'Jindo', 'F', 'white color', 3),
#   Dog('Sachi', 'Siberian Huskey', 'M', 'trouble maker', 0),
#   Dog('Raven', 'Shepherd', 'M', 'friendly', 4)
# ]


# Create your views here.
def home(request):
    """
    this is where we can return a response
    in most cases we render a template
    we'll also need some data for that template in most cases
    """
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def dogs_index(request):
#     dogs = Dog.objects.all()
#     return render(request, 'dogs/index.html', { 'dogs': dogs }) # context object

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # handle the creation of a new user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # this creates a session entry in the database and it persists that session sitewide until the user logs out
            return redirect('index')
        else:
            error_message = 'invalid data - please try again'

    # this is for GET requests, assuming our user clicked on "signup" from the navbar
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class DogIndex(LoginRequiredMixin, ListView):
    model = Dog
    template_name = 'dogs/index.html'
    # displaying only the user's dogs
    def get_queryset(self):
        queryset = Dog.objects.filter(user=self.request.user)
        return queryset

@login_required
def dogs_detail(request, pk):
    dog = Dog.objects.get(id=pk)
    feeding_form = FeedingForm()
    # exclude objects in my toys query that have pk's in this list [1, 4, 5]
    dog_doesnt_have_toys = Toy.objects.exclude(id__in=dog.toys.all().values_list('id'))
    return render(request, 'dogs/detail.html', { 
        'dog': dog, 
        'feeding_form': feeding_form, 
        'notoys': dog_doesnt_have_toys,
    })

# class DogDetail(DetailView):
#     model = Dog, FeedingForm
#     template_name = 'dogs/detail.html'

def add_feeding(request, pk):
    form = FeedingForm(request.POST)
    print(form._errors)
    if form.is_valid():
            new_feeding = form.save(commit=False)
            new_feeding.dog_id = pk
            new_feeding.save()

    return redirect('detail', pk=pk)

# class DeleteFeeding(DeleteView):
#     model = Feeding
#     fields = '__all__'
#     success_url = '/dogs/'

class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ('name', 'breed', 'gender', 'description', 'age')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    # success_url = '/dogs/'

class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    # fields = ('breed', 'gender', 'description', 'age')
    fields = '__all__'

class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs/'

class ToyIndex(ListView):
    model = Toy
    template_name = 'toys/index.html'

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = '__all__'

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'

@login_required
def assoc_toy(request, pk, fk):
    # Note that you can pass a toy's id instead of the whole object
    Dog.objects.get(id=pk).toys.add(fk)
    return redirect('detail', pk=pk)

@login_required
def remove_assoc_toy(request, pk, fk):
    Dog.objects.get(id=pk).toys.remove(fk)
    return redirect('detail', pk=pk)

@login_required
def add_photo(request, pk):
    photo_file = request.FILES.get('photo-file', None)
    
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = Photo(url=url, dog_id=pk)
            photo.save()
        except Exception as error:
            print(f'an error occurred uploading to AWS S3')
            print(error)
    
    return redirect('detail', pk=pk)

# this view will GET and POST request
# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         # handle the creation of a new user
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user) # this creates a session entry in the database and it persists that session sitewide until the user logs out
#             return redirect('index')
#         else:
#             error_message = 'invalid data - please try again'

#     else:
#         # this is for GET requests, assuming our user clicked on "signup" from the navbar
#         form = UserCreationForm()
#         context = {'form': form, 'error_message': error_message}
#         return render(request, 'registration/signup.html', context)
