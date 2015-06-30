from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Shipment
#from .forms import ProductForm

class LoginRequiredMixin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
		return login_required(view)

class ShipmentListView(LoginRequiredMixin, ListView):
	#model = Product
	template_name = 'shipments/shipment_list.html'
	context_object_name = 'shipments'
	paginate_by = 50

	def get_queryset(self):
		return Shipment.objects.all().order_by('-created')

# class ShipmentCreateView(LoginRequiredMixin, CreateView):
# 	model = Shipment
# 	form_class = ProductForm
# 	template_name = "shipments/create_shipment.html"
# 	#success_url = reverse('product_list')
	
# 	def get_success_url(self):
# 		return reverse('shipment_list')

# 	def form_valid(self, form):
# 		form.instance.created_by = self.request.user
# 		return super(ProductCreateView, self).form_valid(form)

class ShipmentDetailView(LoginRequiredMixin, DetailView):
	model = Shipment
	template_name = 'shipments/shipment_detail.html'
	context_object_name = 'shipment'
	pk_url_kwarg = 'pk'
