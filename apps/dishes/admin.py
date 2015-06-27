from django.contrib import admin
from .models import Dish, Ingredient

class IngredientInline(admin.TabularInline):
	model = Ingredient
	raw_id_fields = ("product",)
	extra = 1
	classes = ('collapse open',)

class DishAdmin(admin.ModelAdmin):
	inlines = [IngredientInline,]
	search_fields = ['name',]

admin.site.register(Dish, DishAdmin)
