from django.conf.urls import patterns, url
from .views import StoreListView

urlpatterns = patterns('',
	url(r'^$', StoreListView.as_view(), name='store_list'),
	url(r'^(?P<pk>[0-9]+)/$', StoreDetailView.as_view(), name='store_detail'),
)