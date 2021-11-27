from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.http import HttpResponse
from .models import Dog, Toy, Feeding
from .forms import FeedingForm



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

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def assoc_toy(request, pk, fk):
    # Note that you can pass a toy's id instead of the whole object
    Dog.objects.get(id=pk).toys.add(fk)
    return redirect('detail', pk=pk)

def remove_assoc_toy(request, pk, fk):
    Dog.objects.get(id=pk).toys.remove(fk)
    return redirect('detail', pk=pk)