from django.contrib import admin
from django.contrib.auth.models import User
from .models import Dish, Ingredient, PreDishIngredient

class IngredientInline(admin.TabularInline):
	model = Ingredient
	raw_id_fields = ("product",)
	extra = 1
	classes = ('collapse open',)

class PreDishInline(admin.TabularInline):
	model = PreDishIngredient
	raw_id_fields = ("predish",)
	extra = 1
	classes = ('collapse open',)


class DishAdmin(admin.ModelAdmin):
	inlines = [IngredientInline, PreDishInline]
	search_fields = ['name',]
	fields = ('name', 'team', ('start', 'ex_finish'), ('status', 'weight', 'preserve', 'qty'), ('alergies', 'shipping_form'), 'created_by')
	list_display = ('lotnumber', 'name', 'team', 'status', 'production_date', 'expiration_date')
	list_filter = ['production_date', 'status']

	class Media:
		from django.conf import settings
		static_url = getattr(settings, 'STATIC_URL', '/static')
		js = [static_url+'js/selectandprint.js',]

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'created_by':
			kwargs['queryset'] = User.objects.filter(username=request.user.username)
		return super(DishAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
	def get_readonly_fields(self, request, obj=None):
		if obj is not None:
			return self.readonly_fields + ('created_by', 'created', 'modified','print_tag')
		return self.readonly_fields

	def get_fields(self, request, obj=None):
		if obj is not None:
			return self.fields + (('created', 'modified'), 'print_tag')
		return self.fields
	
	def add_view(self, request, form_url="", extra_context=None):
		data = request.GET.copy()
		data['created_by'] = request.user
		request.GET = data
		return super(DishAdmin, self).add_view(request, form_url="", extra_context=extra_context)



admin.site.register(Dish, DishAdmin)
