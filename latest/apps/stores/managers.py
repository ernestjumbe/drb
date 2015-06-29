from django.db import models

class StoreManager(models.Manager):
	def get_query_set(self):
		return (
			super(StoreManager, self)
			.get_query_set()
			.order_by('name')
		)