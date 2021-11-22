from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

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

    # new method
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
        # return len( self.feeding_set.filter(date=date.today()) )


# Feeding model
class Feeding(models.Model):
    date = models.DateField('Feeding Date')     # change Date: to Feeding Date: on admin page
    meal = models.CharField(
        max_length=1, 
        choices=MEALS, 
        default=MEALS[0][0]
    )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']


# Toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'pk': self.id})
