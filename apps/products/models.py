import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from core.models import TimeStampedModel
from stores.models import Store


STATUS_COLLECTED = 1
STATUS_READY_FOR_USE = 2

STATUS_CHOICES = (
	(STATUS_COLLECTED, _('Collected')),
	(STATUS_READY_FOR_USE, _('Ready for use')),
)

TYPE_INGREDIENT = 1
TYPE_DISH = 2

TYPE_CHOICES = (
	(TYPE_INGREDIENT, _('Ingredient')),
	(TYPE_DISH, _('Dish')),
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
KOLE_CONTAINER_4 = 3
KOLE_CONTAINER_5 = 4
FRYSE_CONTAINER_6 = 5
FRYSE_CONTAINER_7 = 6
ZONE_CONTAINER_1 = 7
ZONE_CONTAINER_2 = 8
ZONE_CONTAINER_3 = 9
ZONE_CONTAINER_4 = 10
ZONE_CONTAINER_5 = 11

POSITION_CHOICES = (
	(NULL, '--------'),
	(KOLERUM_2, u'Kolerum 2'),
	(KOLERUM_3, u'Kolerum 3'),
	(KOLE_CONTAINER_4, u'Kole Container 4'),
	(KOLE_CONTAINER_5, u'Kole Container 5'),
	(FRYSE_CONTAINER_6, 'Fryse Container 6'),
	(FRYSE_CONTAINER_7, 'Fryse Container 7'),
	(ZONE_CONTAINER_1, 'Zone Container 1'),
	(ZONE_CONTAINER_2, 'Zone Container 2'),
	(ZONE_CONTAINER_3, 'Zone Container 3'),
	(ZONE_CONTAINER_4, 'Zone Container 4'),
	(ZONE_CONTAINER_5, 'Zone Container 5'),
)

@python_2_unicode_compatible
class Product(TimeStampedModel):
	qty = models.IntegerField('Antal', blank=True, null=True)
	i_type = models.CharField('Enhed', max_length=50)
	name = models.CharField('Produkt', max_length=100)
	weight_per_item = models.DecimalField('Vaegt pr. enhed (i kg)', max_digits=5, decimal_places=2)
	#lot_number = models.CharField(_('lot number'), max_length=50)
	description = models.TextField(_('description'), null=True, blank=True)
	production_date = models.DateField(_('production date'), blank=True, null=True)
	expiry_date = models.DateField(_('expiry date'))
	date_received = models.DateField(_('date received'), default=datetime.date.today)
	initial_weight = models.DecimalField(_('initial weight'), max_digits=5, decimal_places=2, blank=True, null=True, editable=False)
	current_weight = models.DecimalField(_('current weight'), max_digits=5, decimal_places=2, blank=True, editable=False)
	status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1, help_text=_('What is the current status?'))
	product_type = models.IntegerField(_('product type'), choices=TYPE_CHOICES, default=1)
	preserve = models.IntegerField(_('preserve'), choices=PRESERVE_CHOICES, help_text=_('How should this be preserved?'))
	position = models.IntegerField(_('position'), choices=POSITION_CHOICES, help_text=_('Where has this been stored?'), default=0)
	store = models.ForeignKey(Store)

	def __str__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return('product_detail', (), {'pk': self.pk})

	def __init__(self, *args, **kwargs):
		super(Product, self).__init__(*args, **kwargs)
		self.og_initial_weight = self.initial_weight

	def save(self, *args, **kwargs):
		self.initial_weight = self.qty*self.weight_per_item
		if self.pk is None:
			self.current_weight = self.initial_weight
		else:
			self.current_weight = self.current_weight + (self.initial_weight - self.og_initial_weight)
		super(Product, self).save()

