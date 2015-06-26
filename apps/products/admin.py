from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'product_type', 'status')
	list_display_links = ('name',)


admin.site.register(Product, ProductAdmin)
