from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from core.models import TimeStampedModel

@python_2_unicode_compatible
class Team(TimeStampedModel):
	name = models.CharField(_('name'), max_length=50)

	class Meta:
		verbose_name='team leader'
		verbose_name_plural='team leaders'

	def __str__(self):
		return self.name
