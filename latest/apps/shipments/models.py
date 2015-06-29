from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
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

	def __str__(self):
		return self.destination

@python_2_unicode_compatible
class Batch(models.Model):
	batch = models.ForeignKey(Dish, to_field='lotnumber')
	shipment = models.ForeignKey(Shipment)
	weight = models.DecimalField('vaegt', max_digits=5, decimal_places=2)
	qty = models.IntegerField('Antal', blank=True, null=True)

	def __str__(self):
		return self.batch

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
