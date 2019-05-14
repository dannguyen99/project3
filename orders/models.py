from django.db import models

# Create your models here.
class Pizza(models.Model):
    Regular = 'RL'
    Sicilian = 'SC'
    type_choices = ((Regular,'Regular'), (Sicilian, 'Sicilian'))
    name = models.CharField(max_length=64, default="Italy")
    type = models.CharField(max_length=20, choices = type_choices)
    price_small = models.DecimalField(max_digits=5, decimal_places=2)
    price_large = models.DecimalField(max_digits=5, decimal_places=2,default = 0)
    def __str__(self):
        return f"{self.name} - {self.type} - {self.price_small} - {self.price_large}"

class Topping(models.Model):
    name = models.CharField(max_length = 64)

class Sub(models.Model):
    name = models.CharField(max_length = 64)

class Pasta(models.Model):
    name = models.CharField(max_length = 64)

class Salad(models.Model):
    name = models.CharField(max_length = 64)

class Dinner_Platter(models.Model):
    name = models.CharField(max_length = 64)
