from django.conf.urls import patterns, url
from .views import subscribe_api_view


urlpatterns = patterns(
    '',
    url(r'^subscribe/$', subscribe_api_view, name='api'),
)
