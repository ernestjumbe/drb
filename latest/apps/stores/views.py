from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Store

class LoginRequiredMixin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
		return login_required(view)

class StoreListView(LoginRequiredMixin, ListView):
	model = Store
	context_object_name = 'stores'
	template_name = 'stores/store_list.html'
	paginate_by = 50

class StoreDetailView(LoginRequiredMixin, DetailView):
	model = Store
	context_object_name = 's'
	pk_url_kwarg = 'pk'
	template_name = 'stores/store_detail.html'
