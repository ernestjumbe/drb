from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	#Remember to add Lot number
	list_display = ('id', 'name',  'qty', 'current_weight', 'status', 'product_type', 'preserve', 'position', 'expiry_date')
	list_display_links = ('name',)
	readonly_fields=('current_weight', 'created', 'modified')


admin.site.register(Product, ProductAdmin)
