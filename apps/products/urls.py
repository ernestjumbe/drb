from django.conf.urls import patterns, url, include
from .views import ProductCreateView, ProductListView, ProductDetailView

urlpatterns = patterns('',
	url(r'^$', ProductListView.as_view(), name='product_list'),
	url(r'^(?P<pk>[0-9]+)/$', ProductDetailView.as_view(), name='product_detail'),
	url(r'^create/$', ProductCreateView.as_view(), name='create_product'),
)