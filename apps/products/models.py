import datetime
import random
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from core.models import TimeStampedModel
from stores.models import Store
from django.contrib.auth.models import User


STATUS_COLLECTED = 1
STATUS_IN_HOUSE = 2
STATUS_DISCARDED = 3

STATUS_CHOICES = (
	(STATUS_COLLECTED, _('Collected')),
	(STATUS_IN_HOUSE, _('In House')),
	(STATUS_DISCARDED, _('Discarded')),
)

TYPE_INGREDIENT = 1
TYPE_READY_TO_EAT = 2

TYPE_CHOICES = (
	(TYPE_INGREDIENT, _('Ingredient')),
	(TYPE_READY_TO_EAT, _('Ready to eat')),
)

PRESERVE_REFRIGERATED = 1
PRESERVE_FROZEN = 2
PRESERVE_SHELF = 3

PRESERVE_CHOICES = (
	(PRESERVE_REFRIGERATED, _('Refrigerated')),
	(PRESERVE_FROZEN, _('Frozen')),
	(PRESERVE_SHELF, _('Shelf')),
)

NULL = 0
KOLERUM_2 = 1
KOLERUM_3 = 2
UDGAAENDE_KOEL = 3
HURTIG_NEDKOEL = 4
UDGAAENDE_FRYS = 5
INDGAAENDE_FRYS = 6
CITY_CENTER_EAST = 7
APOLLO_SYD = 8
TRANSIT = 9
SHELF = 10


POSITION_CHOICES = (
	(NULL, '--------'),
	(KOLERUM_2, u'Kolerum 2'),
	(KOLERUM_3, u'Kolerum 3'),
	(UDGAAENDE_KOEL, u'Udgaaende Koel'),
	(HURTIG_NEDKOEL, u'Hurtig Nedkoel'),
	(UDGAAENDE_FRYS, 'Udgaaende Frys'),
	(INDGAAENDE_FRYS, 'Indgaaende Frys'),
	(CITY_CENTER_EAST, 'City Center East'),
	(APOLLO_SYD, 'Apollo Syd'),
	(TRANSIT, 'Transit'),
	(SHELF, 'Shelf')
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
	if not Product.objects.filter(lotnumber=lot).exists():
		print "Lot number exists"
		return lot
	else:
		print lot
		create_lot_number()


@python_2_unicode_compatible
class Product(TimeStampedModel):
	lotnumber = models.CharField(_('Lot number'), max_length=9, editable=False, blank=True, null=True, unique=True)
	qty = models.IntegerField('Antal')
	i_type = models.CharField('Enhed', max_length=50)
	name = models.CharField('Produkt', max_length=100)
	weight_per_item = models.DecimalField('Vaegt pr. enhed (i kg)', max_digits=11, decimal_places=2)
	#lot_number = models.CharField(_('lot number'), max_length=50)
	description = models.TextField(_('description'), null=True, blank=True)
	production_date = models.DateField(_('production date'), blank=True, null=True)
	expiry_date = models.DateField(_('expiry date'))
	date_received = models.DateField(_('date received'), default=datetime.date.today)
	initial_weight = models.DecimalField(_('initial weight'), max_digits=11, decimal_places=2, blank=True, null=True, editable=False)
	current_weight = models.DecimalField(_('current weight'), max_digits=11, decimal_places=2, blank=True, editable=False)
	status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1, help_text=_('What is the current status?'))
	product_type = models.IntegerField(_('product type'), choices=TYPE_CHOICES, default=1)
	preserve = models.IntegerField(_('preserve'), choices=PRESERVE_CHOICES, help_text=_('How should this be preserved?'))
	position = models.IntegerField(_('position'), choices=POSITION_CHOICES, help_text=_('Where has this been stored?'), default=0)
	store = models.ForeignKey(Store)
	created_by = models.ForeignKey(User)

	class Meta:
		ordering = ['created']

	def __str__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return('product_detail', (), {'pk': self.pk})

	def print_tag(self):
		# if self.production_date:
		# 	prod_date = self.production_date
		# else:
		# 	prod_date = '-----'
		if self.expiry_date:
			expr_date = self.expiry_date
		else:
			expr_date = '-----'
		return (u'<div id="printable" onclick="selectText(\'printable\')" style="width: 230px; font-size: 11px; font-weight: bold; line-height: 13px">' \
				 '<span>Det Runde Bord - Stop Spild Af Mad - Roskilde Festival 2015</span> <br>' \
			     '<strong>Lot Number:</strong> %s' \
			     '<br><strong>Item:</strong> %s <br>' \
			     '<strong>Expiry date:</strong> %s' \
			     '</div>' % \
			     (self.lotnumber, \
			     self.name, \
			     expr_date))

	print_tag.short_description = 'Label'
	print_tag.allow_tags=True

	def __init__(self, *args, **kwargs):
		super(Product, self).__init__(*args, **kwargs)
		self.og_initial_weight = self.initial_weight

	def save(self, *args, **kwargs):
		self.initial_weight = self.qty*self.weight_per_item
		if self.pk is None:
			self.current_weight = self.initial_weight
			#lotnumber = create_lot_number()

			#print create_lot_number()
			self.lotnumber = create_lot_number()
		else:
			self.current_weight = self.current_weight + (self.initial_weight - self.og_initial_weight)
			
		super(Product, self).save()

