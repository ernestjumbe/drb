from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Store

class StoreListView(ListView):
	model = Store
	context_object_name = 'stores'
	template_name = 'stores/store_list.html'
	paginate_by = 50

class StoreDetailView(DetailView):
	model = Store
	context_object_name = 's'
	pk_url_kwarg = 'pk'
	template_name = 'stores/store_detail.html'
