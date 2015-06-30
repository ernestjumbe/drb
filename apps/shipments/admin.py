from django.contrib import admin
from .models import Shipment, Batch, Ingredient

class BatchInline(admin.TabularInline):
	model = Batch
	raw_id_fields = ("batch",)
	extra = 1
	classes = ('collapse open',)

class IngredientInline(admin.TabularInline):
	model = Ingredient
	raw_id_fields = ("product",)
	extra = 1
	classes = ('collapse open',)

class ShipmentAdmin(admin.ModelAdmin):
	inlines = [BatchInline, IngredientInline]
	search_fields = ['destination']
	list_display = ('id', 'destination', 'departure', 'driver')
	list_display_links = ('destination',)

admin.site.register(Shipment, ShipmentAdmin)
