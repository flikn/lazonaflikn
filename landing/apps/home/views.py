# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth import get_user_model
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from .mixins import LoginRequiredMixin
from apps.customuser.forms import UserSignupForm, UserLoginForm


class HomeView(TemplateView):
    template_name = "home/home.html"


class ThanksView(LoginRequiredMixin, TemplateView):
    template_name = "home/thanks.html"


def subscribe_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home_app:signup'))

    if request.user.was_registered:
        return HttpResponseRedirect(reverse('home_app:thanks'))

    return render_to_response(
        'home/subscribe.html',
        context_instance=RequestContext(request),
    )


def signup_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home_app:subscribe'))

    message = ""
    if request.method == "POST":
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            MyUser = get_user_model()
            new_user = MyUser.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home_app:subscribe'))
        message = "Cuenta no es valida."

    ctx = {
        'message': message,
    }
    return render_to_response(
        'home/signup.html',
        ctx,
        context_instance=RequestContext(request),
    )


def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home_app:subscribe'))

    message = ""
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home_app:subscribe'))
        message = "Contraseña o Usuario Incorrecto."

    ctx = {
        'message': message,
    }
    return render_to_response(
        'home/login.html',
        ctx,
        context_instance=RequestContext(request),
    )


def logout_view(request):
    logout(request)
    return redirect('http://www.flikn.com/cursos/todos/nuevos')
