from django.conf.urls import patterns, url
from .views import subscribe_view


urlpatterns = patterns(
    '',
    url(r'^subscribe/$', subscribe_view, name='api'),
)
