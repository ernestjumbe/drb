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

@python_2_unicode_compatible
class Product(TimeStampedModel):
	name = models.CharField(_('name of product'), max_length=100)
	#lot_number = models.CharField(_('lot number'), max_length=50)
	description = models.TextField(_('description'), null=True, blank=True)
	production_date = models.DateField(_('production date'), default=datetime.date.today)
	expiry_date = models.DateField(_('expiry date'))
	date_received = models.DateField(_('date received'), default=datetime.date.today)
	#weight = models.IntegerField(_('weight of package'), help_text=_('Weight in grams'))
	initial_weight = models.DecimalField(_('initial weight'), max_digits=5, decimal_places=2)
	current_weight = models.DecimalField(_('current weight'), max_digits=5, decimal_places=2, blank=True)
	status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1, help_text=_('What is the current status?'))
	product_type = models.IntegerField(_('product type'), choices=TYPE_CHOICES, default=1)
	preserve = models.IntegerField(_('preserve'), choices=PRESERVE_CHOICES, help_text=('How should this be preserved?'))
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
		if self.pk is None:
			self.current_weight = self.initial_weight
		else:
			self.current_weight = self.current_weight + (self.initial_weight - self.og_initial_weight)
		super(Product, self).save()

