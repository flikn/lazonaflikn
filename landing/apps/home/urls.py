from django.conf.urls import patterns, url
from .views import HomeView, LoginView, SignupView, SubscribeView
from .views import ThanksView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^subscribe/$', SubscribeView.as_view(), name="subscribe"),
)
