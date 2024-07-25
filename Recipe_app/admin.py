from django.contrib import admin

from Recipe_app.models import List, Recipes, FoodType

admin.site.register(List)
admin.site.register(Recipes)
admin.site.register(FoodType)

# Register your models here.
