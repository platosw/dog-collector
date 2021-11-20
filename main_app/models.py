from django.db import models
from django.urls import reverse
# Create your models here.

# Dog model
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    description = models.TextField(max_length=500)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'dog_id': self.id})

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})


# Toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name