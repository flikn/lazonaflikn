from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    # Grappelli url.
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/',  include(admin.site.urls)),
    # Subscribe app.
    url(r'^api/', include('apps.subscribe.urls', namespace='subscribe_app')),
    # Home app.
    url(r'^', include('apps.home.urls', namespace='home_app')),
    # Customuser app.
    url(r'^', include('apps.customuser.urls', namespace='customuser_app')),
    # Python social auth.
    url('', include('social.apps.django_app.urls', namespace='social')),
)
