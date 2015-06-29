import itertools
from django import forms
from django.forms.models import BaseFormSet, formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import ugettext as _
from .models import Dish, Ingredient
from teams.models import Team

# class DishForm(forms.Form):
# 	blank_choice = [('',_('Chose a team'))]
# 	TEAM_CHOICES = Team.objects.all()
# 	name = forms.CharField()
# 	team = forms.ChoiceField(widget=forms.Select(),
# 		                     choices=(itertools.chain(blank_choice, ((x.name, x.name) for x in TEAM_CHOICES))))

class DishForm(forms.ModelForm):
	class Meta:
		model = Dish
		fields = '__all__'

class IngredientForm(forms.Form):

	name = forms.CharField()
	qty_used = forms.IntegerField(label=_('Quantity Used'))

IngrdientFormset = formset_factory(IngredientForm, extra=1)
