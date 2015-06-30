from django.db import models
import random
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

def get_year():
	year = datetime.datetime.now().strftime('%y')
	return year

def create_lot_number():
	sep = "-"
	ran_num = random.randint(0,9999)
	ran_num = str(ran_num).zfill(4)
	seq = ("x", ran_num, str(get_year()))
	lot = sep.join(seq)
	if not Dish.objects.filter(lotnumber=lot).exists():
		return lot
	else:
		print lot
		create_lot_number()
 
@python_2_unicode_compatible
class Dish(TimeStampedModel):
	name = models.CharField(_('name dish'), max_length=100)
	lotnumber = models.CharField(_('Lot number'), max_length=9, editable=False, blank=True, null=True, unique=True)
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

	def print_tag(self):
		if self.production_date:
			prod_date = self.production_date
		else:
			prod_date = '-----'
		if self.expiration_date:
			expr_date = self.expiration_date
		else:
			expr_date = '-----'
		return (u'<div id="printable" onclick="selectText(\'printable\')" style="width: 230px, font-size: 11px, font-weight: normal">' \
				 '<span>Det Runde Bord - Stope Spild Af Mad - Roskilde Festival 2015</span> <br>' \
			     '<strong>Lot Number:</strong> %s' \
			     '<br><strong>Item:</strong> %s <br>' \
			     '<strong>Prod date:</strong> %s <br>' \
			     '<strong>Expiry date:</strong> %s <br>' \
			     '<strong>Allergener:</strong> %s' \
			     '</div>' % \
			     (self.lotnumber, \
			     self.name, \
			     prod_date, \
			     expr_date, \
			     self.alergies))

	print_tag.short_description = 'Label'
	print_tag.allow_tags=True

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.lotnumber = create_lot_number()
		super(Dish, self).save()

@python_2_unicode_compatible
class Ingredient(TimeStampedModel):
	name = models.CharField(_('name'), max_length=100, blank=True, null=True)
	qty_used = models.IntegerField(_('quantity used'), blank=True, null=True)
	weight_used = models.DecimalField(_('weight used'), max_digits=5, decimal_places=2, help_text=_('Enter amount in kgs'))
	dish = models.ForeignKey(Dish)
	product = models.ForeignKey(Product, to_field='lotnumber')

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
			self.lotnumber = create_lot_number()
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
