from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Store

class StoreListView(ListView):
	model = Store
	context_object_name = 'stores'

class StoreDetailView(DetailView):
	model = Store
	context_object_name = 'store'
	pk_url_kwarg = 'pk'
