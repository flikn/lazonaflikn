from django.conf.urls import patterns, url
from .views import HomeView, LoginView, SignupView, SubscribeView


urlpatterns = patterns(
    '',
    url(r'^$', SignupView.as_view(), name="signup"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^subscribe/$', SubscribeView.as_view(), name="subscribe"),
)
