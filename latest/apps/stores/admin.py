from django.contrib import admin
from .models import Store

class StoreAdmin(admin.ModelAdmin):
	list_display = ("name", "camp", "inner_camp")

admin.site.register(Store, StoreAdmin)
