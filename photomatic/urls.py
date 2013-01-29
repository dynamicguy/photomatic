from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

from photomatic.views import *
from photomatic.facebook import facebook_view


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photomatic.views.home', name='home'),
    # url(r'^photomatic/', include('photomatic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', home, name='home'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^form/$', form, name='form'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fb/', facebook_view, name='fb_photomatic'),
    url(r'^close_login_popup/$', close_login_popup, name='login_popup_close'),
    url(r'', include('social_auth.urls')),
    url(r'^albums/$', albums, name='albums'),
    url(r'^albums/(?P<album_id>\d+)/$', album_detail, name='album_detail'),
    url(r'^photos/$', photos, name='photos'),
    url(r'^photos/(?P<photo_id>\d+)/$', photo_detail, name='photo_detail'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)