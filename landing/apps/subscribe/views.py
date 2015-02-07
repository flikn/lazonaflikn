import requests
import json
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Subscriptor


URL = "http://198.143.158.218:28080/ZonaDelSaber/validarCliente.action"


def subscribe_api_view(request):
    if not request.user.is_authenticated():
        return HttpResponse('Unauthorized', status=401)

    data = {}
    if request.user.was_registered:
        data["message"] = "the client have subscribed already"
        data["code"] = 403
        return JsonResponse(data)

    if request.method == "POST":
        client = request.POST.get("client", "")
        account = request.POST.get("account", "")
    else:
        client = request.GET.get("client", "")
        account = request.GET.get("account", "")

    payload = {
        "cliente": client,
        "cuenta": account,
    }
    headers = {
        "User-agent": "Mozilla/5.0",
    }

    try:
        response = requests.get(URL, params=payload, headers=headers)
        data = response.json()
        data["code"] = int(data.get("code"))

        User = get_user_model()
        user = User.objects.get(email=request.user.email)
    except Exception, e:
        data["message"] = "the request is syntactically incorrect"
        data["code"] = 400

    if data.get("code") != 200:
        return JsonResponse(data)

    try:
        subscriptor = Subscriptor.objects.filter(
            client=client,
            account=account,
        )[0]
        if not subscriptor.is_active:
            data["message"] = "the client have subscribed already"
            data["code"] = 403
            return JsonResponse(data)
    except Exception, e:
        subscriptor = None

    if request.method == "POST":
        if not subscriptor:
            subscriptor = Subscriptor.objects.create(
                client=client,
                account=account,
            )
        subscriptor.lifetime -= 1
        subscriptor.save()
        user.subscriptor = subscriptor
        user.save()
        data["lifetime"] = subscriptor.lifetime

    return JsonResponse(data)
