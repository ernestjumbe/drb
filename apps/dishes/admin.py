from django.contrib import admin
from .models import Dish, Ingredient

class IngredientInline(admin.StackedInline):
	model = Ingredient
	raw_id_fields = ("product",)
	extra = 1

class DishAdmin(admin.ModelAdmin):
	inlines = [IngredientInline,]
	search_fields = ['name',]

admin.site.register(Dish, DishAdmin)
