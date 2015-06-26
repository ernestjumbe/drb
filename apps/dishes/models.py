from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from core.models import TimeStampedModel
from products.models import Product
from teams.models import Team

# Create your models here.
# 
@python_2_unicode_compatible
class Dish(TimeStampedModel):
	name = models.CharField(_('name'), max_length=100)
	# lot_number = models.CharField(_('lot number'), max_length=50)
	team = models.ForeignKey(Team)

	def __str__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return('dish_detail', (), {'pk': self.pk})

@python_2_unicode_compatible
class Ingredient(TimeStampedModel):
	name = models.CharField(_('name'), max_length=100)
	qty_used = models.IntegerField(_('quantity used'), blank=True, null=True)
	weight_user = models.IntegerField(_('weight used'), blank=True, null=True)
	dish = models.ForeignKey(Dish)
	product = models.ForeignKey(Product, limit_choices_to={'product_type': 1})

	def __str__(self):
		return self.name
