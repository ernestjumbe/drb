from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from core.models import TimeStampedModel
from products.models import Product
from teams.models import Team
from django.contrib.auth.models import User

STATUS_COOKING = 1
STATUS_COOLING_DOWN = 2
STATUS_READY_FOR_SHIPPING = 3

STATUS_CHOICES = (
	(STATUS_COOKING, 'Cooking'),
	(STATUS_COOLING_DOWN, 'Cool Down'),
	(STATUS_READY_FOR_SHIPPING, 'Ready for shipping')
)

PRESERVE_OPBEVARES_TOERT = 1
PRESERVE_SAETTES_PAA_KOEL = 2
PRESERVE_FRYSES_NED = 3

PRESERVE_CHOICES = (
	(PRESERVE_OPBEVARES_TOERT, 'Opbevares toert'),
	(PRESERVE_SAETTES_PAA_KOEL, 'Saettes paa koel'),
	(PRESERVE_FRYSES_NED, 'Fryses ned')
)
 
@python_2_unicode_compatible
class Dish(TimeStampedModel):
	name = models.CharField(_('name dish'), max_length=100)
	# lot_number = models.CharField(_('lot number'), max_length=50)
	team = models.ForeignKey(Team)
	start = models.DateTimeField('start tidspunkt', default=datetime.datetime.now)
	ex_finish = models.DateTimeField('Forventet klar', blank=True, null=True)
	weight = models.IntegerField(_('vaegt'), blank=True, null=True)
	production_date = models.DateField('produceret den', default=datetime.date.today)
	status = models.IntegerField(_('Status'), choices=STATUS_CHOICES, default=1)
	expiration_date = models.DateField('Udloebsdato', blank=True, null=True)
	preserve = models.IntegerField('Opbevaring', blank=True, null=True)
	shipping_form = models.TextField('Form', blank=True, null=True)
	alergies = models.TextField('Allergener', blank=True, null=True)
	created_by = models.ForeignKey(User)

	class Meta:
		verbose_name='dish'
		verbose_name_plural='dishes'

	def __str__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return('dish_detail', (), {'pk': self.pk})

@python_2_unicode_compatible
class Ingredient(TimeStampedModel):
	name = models.CharField(_('name'), max_length=100, blank=True, null=True)
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
			self.name = p.name
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
