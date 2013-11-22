from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from products import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('products.views',
    url(r'^$', views.home()),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^product_edit/(?P<product_id>\d+)', views.edit_product),
    url(r'^logout/', logout)
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)