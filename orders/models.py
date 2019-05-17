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
    quote = models.CharField(max_length = 1000, default= "Delicous")
    url = models.CharField(max_length = 1000, default = "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/dc23cd051d2249a5903d25faf8eeee4c/BFV36537_CC2017_2IngredintDough4Ways-FB.jpg?output-quality=60&resize=1000:*")
    def __str__(self):
        return f"{self.name} - {self.type} - {self.price_small} - {self.price_large}"

class Topping(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name

class Sub(models.Model):
    name = models.CharField(max_length = 64)
    price_small = models.DecimalField(max_digits=5, decimal_places=2)
    price_large = models.DecimalField(max_digits=5, decimal_places=2,default = 0)
    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"

class Pasta(models.Model):
    name = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.CharField(max_length = 1000, default = "/static/orders/images/pasta-1.jpg")

class Salad(models.Model):
    name = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.CharField(max_length = 1000, default = "https://www.tasteofhome.com/wp-content/uploads/2017/10/Armenian-Garden-Salad_exps47594_TH2236620A05_31_3bC_RMS-1.jpg")

class Dinner_Platter(models.Model):
    name = models.CharField(max_length = 64)
    price_small = models.DecimalField(max_digits=5, decimal_places=2)
    price_large = models.DecimalField(max_digits=5, decimal_places=2,default = 0)
    url = models.CharField(max_length = 1000, default = "/static/orders/images/pasta-1.jpg")
