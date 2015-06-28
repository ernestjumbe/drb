from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
	#model = Product
	template_name = 'products/product_list.html'
	context_object_name = 'products'
	paginate_by = 50

	def get_queryset(self):
		return Product.objects.all().order_by('-date_received')

class ProductCreateView(CreateView):
	model = Product
	form_class = ProductForm
	template_name = "products/create_product.html"
	#success_url = reverse('product_list')
	
	def get_success_url(self):
		return reverse('product_list')

class ProductDetailView(DetailView):
	model = Product
	template_name = 'products/product_detail.html'
	context_object_name = 'product'
	pk_url_kwarg = 'pk'
