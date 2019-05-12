from django.db import models

# Create your models here.
class Pizza(models.model):
    size = models.CharField(max_length=5)
    type = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2)
