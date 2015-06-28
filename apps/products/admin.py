from django.contrib import admin
from django.contrib.auth.models import User
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	#Remember to add Lot number
	list_display = ('lotnumber', 'name',  'qty', 'i_type', 'current_weight', 'status', 'product_type', 'preserve', 'position', 'expiry_date')
	list_display_links = ('name',)
	readonly_fields=('current_weight', 'initial_weight', 'created', 'modified')
	fields = (('qty', 'i_type', 'name', 'weight_per_item'), ('store', 'initial_weight', 'current_weight'), ('production_date', 'date_received', 'expiry_date'), ('status', 'product_type', 'preserve', 'position'), 'description', ('created', 'modified'), 'created_by')

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'created_by':
			kwargs['queryset'] = User.objects.filter(username=request.user.username)
		return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
	def get_readonly_fields(self, request, obj=None):
		if obj is not None:
			return self.readonly_fields + ('created_by',)
		return self.readonly_fields
	
	def add_view(self, request, form_url="", extra_context=None):
		data = request.GET.copy()
		data['created_by'] = request.user
		request.GET = data
		return super(ProductAdmin, self).add_view(request, form_url="", extra_context=extra_context)


admin.site.register(Product, ProductAdmin)
