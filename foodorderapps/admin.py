from django.contrib import admin

# Register your models here.
from .models import FoodType

admin.site.register(FoodType)