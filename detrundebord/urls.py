from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from core.forms import LoginForm
from django.contrib import admin

from core.views import signin, signout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), {}, name='index'),
    url(r'^products/', include('products.urls')),
    url(r'^dishes/', include('dishes.urls')),
    url(r'^stores/', include('stores.urls')),
    url(r'^shipment/', include('shipments.urls')),

    url(r'^login/$',
           signin,
           {
               'form_class': LoginForm
           },
           name='signin'
    ),
    url(r'^disabled/$', TemplateView.as_view(template_name="disabled.html"), {}, name='user_disabled'),
    url(r'^logout/$',
           signout, name='signout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
