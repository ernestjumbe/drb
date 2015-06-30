from django.conf.urls import url, patterns
from .views import ShipmentDetailView, ShipmentListView
urlpatterns = patterns('',
	url(r'^(?P<pk>[0-9]+)/$', ShipmentDetailView.as_view(), name='shipment_detail'),
	#url(r'^create/$', ShipmentDetailView.as_view(), name='shipment_detail'),
	url(r'^$', ShipmentListView.as_view(), name='shipment_list'),
)