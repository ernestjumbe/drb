from django.conf.urls import patterns, url
from .views import DishListView, DishDetailView, DishCreateView
urlpatterns = patterns('',
	url(r'^$', DishListView.as_view(), name='dish_list'),
	url(r'^(?P<pk>[0-9]+)/$', DishDetailView.as_view(), name='dish_detail'),
	url(r'^create/$', DishCreateView.as_view(), name='create_dish'),
)
