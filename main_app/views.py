from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.http import HttpResponse
from .models import Dog, Toy



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

class DogIndex(ListView):
    model = Dog
    template_name = 'dogs/index.html'

# def dogs_detail(request, dog_id):
#     dog = Dog.objects.get(id=dog_id)
#     return render(request, 'dogs/detail.html', { 'dog': dog })

class DogDetail(DetailView):
    model = Dog
    template_name = 'dogs/detail.html'

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    # success_url = '/dogs/'

class DogUpdate(UpdateView):
    model = Dog
    # fields = ('breed', 'gender', 'description', 'age')
    fields = '__all__'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

class ToyIndex(ListView):
    model = Toy
    template_name = 'toys/index.html'