from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home/home.html"


class SignupView(TemplateView):
    template_name = "home/signup.html"


class LoginView(TemplateView):
    template_name = "home/login.html"


class SubscribeView(TemplateView):
    template_name = "home/subscribe.html"
