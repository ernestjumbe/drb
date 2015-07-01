from django.contrib import admin
from django.contrib.auth.models import User
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

	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'user':
			kwargs['queryset'] = User.objects.filter(username=request.user.username)
		return super(ShipmentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
	def get_readonly_fields(self, request, obj=None):
		if obj is not None:
			return self.readonly_fields + ('user',)
		return self.readonly_fields
	
	# def get_fields(self, request, obj=None):
	# 	if obj is not None:
	# 		return self.fields + (('created', 'modified'),)
	# 	return self.fields
	
	def add_view(self, request, form_url="", extra_context=None):
		data = request.GET.copy()
		data['user'] = request.user
		request.GET = data
		return super(ShipmentAdmin, self).add_view(request, form_url="", extra_context=extra_context)

admin.site.register(Shipment, ShipmentAdmin)
