from django.db import models
from django.utils.translation import uggetext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from phonenumber_field.modelfields import PhoneNumberField
from core.models import TimeStampedModel

class Destination(TimeStampedModel):
	name = models.CharField(_('name'), max_length=254)
	phone_number = PhoneNumberField(_('phone number'))
	email = models.EmailField(_('email'), max_length=254)
	contact_name = models.CharField(_('contact name'), max_length=254)

	def __str__(self):
		return self.name
