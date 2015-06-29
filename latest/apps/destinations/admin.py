from django.contrib import admin
from .models import Destination

class DestinationAdmin(admin.ModelAdmin):
	list_display = ("name", "phone_number", "email", "contact_name")

admin.site.register(Destination, DestinationAdmin)
