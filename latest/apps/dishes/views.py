from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.forms.util import ValidationError
from crispy_forms.helper import FormHelper, Layout
from .models import Dish
from .forms import DishForm, IngrdientFormset

class LoginRequiredMixin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
		return login_required(view)

class DishListView(LoginRequiredMixin, ListView):
	model = Dish
	context_object_name = 'dishes'
	template_name = 'dishes/dish_list.html'

class DishDetailView(LoginRequiredMixin, DetailView):
	model = Dish
	context_object_name = 'dish'
	pk_url_kwarg = 'pk'
	template_name = 'dishes/dish_detail.html'

class IngredientFormSetHelper(FormHelper):
	def __init__(self, *args, **kwargs):
		super(IngredientFormSetHelper, self).__init__(*args, **kwargs)
		self.form_tag = False
		self.disable_csrf = True
		self.layout = Layout('form_ingredient')
		self.render_required_fields = True

class DishCreateView(LoginRequiredMixin, CreateView):
	model = Dish
	form_class = DishForm
	template_name = 'dishes/create_dish.html'

	def get(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		ingredient_form = IngrdientFormset()
		helper = IngredientFormSetHelper()
		return self.render_to_response(
			self.get_context_data(form=form,
				ingredient_form=ingredient_form,
				helper=helper))

