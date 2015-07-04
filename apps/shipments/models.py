from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from products.models import Product
from core.models import TimeStampedModel
from dishes.models import Dish
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Shipment(TimeStampedModel):
	#delivery ID
	id = models.AutoField(_('Delivery ID'), primary_key=True)
	destination = models.CharField('destination', max_length=254)
	driver = models.CharField('Chauffeur', max_length=150)
	departure = models.DateTimeField('Afgangstidspunkt', default=datetime.datetime.now)
	user = models.ForeignKey(User)

	class Meat:
		verbose_name='Delivery'
		verbose_name_plural='Deliveries'

	def __str__(self):
		return self.destination

	@models.permalink
	def get_absolute_url(self):
		return('shipment_detail', (), {'pk': self.pk})


class Batch(models.Model):
	batch = models.ForeignKey(Dish, to_field='lotnumber')
	shipment = models.ForeignKey(Shipment)
	weight = models.DecimalField('vaegt', max_digits=5, decimal_places=2, blank=True, null=True, default=0.0)
	qty = models.IntegerField('Antal', blank=True, null=True)

	class Meta:
		verbose_name=_('Dish')
		verbose_name_plural=_('Dishes')

	

	def __init__(self, *args, **kwargs):
		super(Batch, self).__init__(*args, **kwargs)
		self.og_weight = self.weight

	def save(self, *args, **kwargs):
		if self.pk is None:
			d = Dish.objects.get(pk=self.batch.pk)
			d.weight = d.weight - self.weight
			d.save()
		else:
			d = Dish.objects.get(pk=self.batch.pk)
			d.weight = d.weight + (self.og_weight - self.weight)
			d.save()
		super(Batch, self).save()

	def delete(self, *args, **kwargs):
		d = Dish.objects.get(pk=self.batch.pk)
		d.weight = d.weight + self.og_weight
		d.save()
		super(Batch, self).delete()

@python_2_unicode_compatible
class Ingredient(TimeStampedModel):
	name = models.CharField(_('name'), max_length=100, blank=True, null=True)
	qty_used = models.IntegerField(_('quantity used'), blank=True, null=True)
	weight_used = models.DecimalField(_('weight used'), max_digits=5, decimal_places=2, help_text=_('Enter amount in kgs'), blank=True, null=True)
	shipment = models.ForeignKey(Shipment)
	product = models.ForeignKey(Product, to_field='lotnumber', related_name='ship_ingredient')

	def __str__(self):
		return self.name


	def __init__(self, *args, **kwargs):
		super(Ingredient, self).__init__(*args, **kwargs)
		self.og_weight_used = self.weight_used

	# def save(self, *args, **kwargs):
	# 	if self.pk is None:
	# 		p = Product.objects.get(pk=self.product.pk)
	# 		p.current_weight = p.current_weight - self.weight_used
	# 		p.save()
	# 		self.name = p.name
	# 		self.lotnumber = create_lot_number()
	# 	else:
	# 		p = Product.objects.get(pk=self.product.pk)
	# 		p.current_weight = p.current_weight + (self.og_weight_used - self.weight_used)
	# 		p.save()
	# 	super(Ingredient, self).save()

	# def delete(self, *args, **kwargs):
	# 	p = Product.objects.get(pk=self.product.pk)
	# 	p.current_weight = p.current_weight + self.og_weight_used
	# 	p.save()
	# 	super(Ingredient, self).delete()

