from django.conf.urls import patterns, url
from .views import HomeView, ThanksView
from .views import logout_view, login_view, signup_view, subscribe_view


urlpatterns = patterns(
    '',
    url(r'^$', signup_view, name="signup"),
    url(r'^signup/$', signup_view, name="signup"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^subscribe/$', subscribe_view, name="subscribe"),
    url(r'^thanks/$', ThanksView.as_view(), name="thanks"),
)
