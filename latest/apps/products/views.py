from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

class LoginRequiredMixin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
		return login_required(view)

class ProductListView(LoginRequiredMixin, ListView):
	#model = Product
	template_name = 'products/product_list.html'
	context_object_name = 'products'
	paginate_by = 50

	def get_queryset(self):
		return Product.objects.all().order_by('-date_received')

class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	form_class = ProductForm
	template_name = "products/create_product.html"
	#success_url = reverse('product_list')
	
	def get_success_url(self):
		return reverse('product_list')

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(ProductCreateView, self).form_valid(form)

class ProductDetailView(LoginRequiredMixin, DetailView):
	model = Product
	template_name = 'products/product_detail.html'
	context_object_name = 'product'
	pk_url_kwarg = 'pk'
