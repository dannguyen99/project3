from django.contrib import admin
from .models import Pizza, Topping, Sub, Pasta, Salad
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
