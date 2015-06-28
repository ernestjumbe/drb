from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from phonenumber_field.modelfields import PhoneNumberField
from core.models import TimeStampedModel
from .managers import StoreManager

CAMP_BERENDSEN = 1
CAMP_CAMPING_EAST_AGORA_H = 2
CAMP_CAMPING_EAST_AGORA_J = 3
CAMP_CAMPING_EAST_AGORA_L = 4
CAMP_CAMPING_EAST_AGORA_M = 5
CAMP_CAMPING_EAST_BYCENTER_N = 6
CAMP_CAMPING_EAST_BYCENTER_S = 7
CAMP_CAMPING_EAST_SUPER_G = 8
CAMP_CAMPING_WEST_AGORA_C = 9
CAMP_CAMPING_WEST_BYCENTER = 10
CAMP_CAMPING_WEST_SKATE = 11
CAMP_FOOD_TRUCK = 12
CAMP_ARENA = 13
CAMP_ARTIST_VILLAGE = 14
CAMP_AVALON = 15
CAMP_BACKALLEY = 16
CAMP_BACKSTAGE_VILLAGE = 17
CAMP_FOOD_COURT = 18
CAMP_GLORIA = 19
CAMP_GLORIA_SCENEN = 20
CAMP_HANDELSOEEN = 21
CAMP_INDRE_OG_YDRE = 22
CAMP_LUKKET_OMRAADE = 23
CAMP_PAVILION = 24
CAMP_STREET_ART = 25
CAMP_TRADE_ZONE = 26
CAMP_VED_SEJLENE = 27

CAMP_CHOICES = (
	(CAMP_BERENDSEN, 'Brendsen'),
	(CAMP_CAMPING_EAST_AGORA_H, 'Camping East/Agora H'),
	(CAMP_CAMPING_EAST_AGORA_J, 'Camping East/Agora J'),
	(CAMP_CAMPING_EAST_AGORA_L, 'Camping East/Agora L'),
	(CAMP_CAMPING_EAST_AGORA_M, 'Camping East/Agora M'),
	(CAMP_CAMPING_EAST_BYCENTER_N, 'Camping East/Bycenter N'),
	(CAMP_CAMPING_EAST_BYCENTER_S, 'Camping East/Bycenter S'),
)

@python_2_unicode_compatible
class Store(TimeStampedModel):
	list_number = models.CharField(_('list number'), max_length=50)
	name = models.CharField(_('name'), max_length=254)
	phone_number = PhoneNumberField(_('phone number'), blank=True, null=True)
	contact_email = models.EmailField(_('email'), max_length=254)
	contact_fname = models.CharField(_('Contact First name'), max_length=254)
	contact_lname = models.CharField(_('Contact Last name'), max_length=254)
	company_name = models.CharField(_('Company name'), max_length=254)
	company_adress = models.CharField(_('company address'), max_length=50)
	company_postcode = models.CharField(_('company postcode'), max_length=11)
	company_town = models.CharField(_('company town'), max_length=50)
	company_country = models.CharField(_('company country'), max_length=254, default='Danmark')
	camp = models.CharField(_('camp'), max_length=100)
	inner_camp = models.CharField(_('inner camp'), max_length=1)
	other_drinks = models.TextField(_('other drinks'))
	taxable_drinks = models.TextField(_('taxable drinks'))
	assortment = models.TextField(_('assortment'))
	objects = StoreManager()

	class Meta:
		ordering =['name']


	def __str__(self):
		return ('%s - %s, %s' % (self.name, self.camp, self.inner_camp))

	@models.permalink
	def get_absolute_url(self):
		return('store_detail', (), {'pk': self.pk})
