from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from .models import Product 


class ProductListView(ListView):
	#model = Product
	template_name = 'products/product_list.html'
	context_object_name = 'products'
	paginate_by = 50

	def get_queryset(self):
		return Product.objects.all().order_by('-date_received')

class ProductCreateView(CreateView):
	model = Product
	fields = ['name', 'production_date', 'expiry_date', 'weight', 'status', 'preserve', 'source']
	template_name = "products/create_product.html"

class ProductDetailView(DetailView):
	model = Product
	template_name = 'products/product_detail.html'
	context_object_name = 'product'
	pk_url_kwarg = 'pk'
