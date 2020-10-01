from django.db import models
import datetime

# Create your models here.


class Car(models.Model):
    all_years = [r for r in range(2000, datetime.datetime.now().year + 2)]
    default_year = datetime.datetime.now().year

    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=32, choices=['used', 'new'])
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    miles = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(
        max_length=32, choices=['manual', 'automatic'])
    year = models.IntegerField(
        choices=all_years, default=default_year
    )
    power = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    description = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'car: {self.brand} is {self.category}'
