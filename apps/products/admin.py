from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	#Remember to add Lot number
	list_display = ('id', 'name',  'qty', 'current_weight', 'status', 'product_type', 'preserve', 'position')
	list_display_links = ('name',)
	readonly_fields=('current_weight', 'initial_weight')
	fields = (('qty', 'i_type', 'name', 'weight_per_item'), ('store', 'initial_weight', 'current_weight'), ('production_date', 'date_received', 'expiry_date'), ('status', 'preserve', 'position'), 'description')


admin.site.register(Product, ProductAdmin)
