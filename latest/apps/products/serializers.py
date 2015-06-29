from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('name', 'description', 'weight',
			      'preserve', 'status', 'product_type',
			      'date_received', 'production_data', 'expiry_date',
			      'store')
