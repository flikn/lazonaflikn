from django.conf.urls import patterns, url
from .views import require_extra_data


urlpatterns = patterns(
    '',
    url(r'^complete-signup/$', require_extra_data, name='complete-signup'),
)
