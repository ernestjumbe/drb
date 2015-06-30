from django.contrib import admin
from .models import Shipment, Batch

class BatchInline(admin.TabularInline):
	model = Batch
	raw_id_fields = ("batch",)
	extra = 1
	classes = ('collapse open',)

class ShipmentAdmin(admin.ModelAdmin):
	inlines = [BatchInline]
	search_fields = ['destination']
	list_display = ('id', 'destination', 'departure', 'driver')
	list_display_links = ('destination',)

admin.site.register(Shipment, ShipmentAdmin)
