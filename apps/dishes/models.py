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
	weight_used = models.DecimalField(_('weight used'), max_digits=5, decimal_places=2, help_text=_('Enter amount in kgs'))
	dish = models.ForeignKey(Dish)
	product = models.ForeignKey(Product, limit_choices_to={'product_type': 1})

	def __str__(self):
		return self.name

	def __init__(self, *args, **kwargs):
		super(Ingredient, self).__init__(*args, **kwargs)
		self.og_weight_used = self.weight_used

	def save(self, *args, **kwargs):
		if self.pk is None:
			p = Product.objects.get(pk=self.product.pk)
			p.current_weight = p.current_weight - self.weight_used
			p.save()
		else:
			p = Product.objects.get(pk=self.product.pk)
			p.current_weight = p.current_weight + (self.og_weight_used - self.weight_used)
			p.save()
		super(Ingredient, self).save()

	def delete(self, *args, **kwargs):
		p = Product.objects.get(pk=self.product.pk)
		p.current_weight = p.current_weight + self.og_weight_used
		p.save()
		super(Ingredient, self).delete()
