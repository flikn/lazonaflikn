import requests
import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscriptor


URL = "http://198.143.158.218:28080/ZonaDelSaber/validarCliente.action"


def subscribe_view(request):
    data = {}

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
        if data.get("code") == 200:
            try:
                if Subscriptor.objects.get(client=client) or \
                        Subscriptor.objects.get(account=account):
                    data["message"] = "the client have subscribed already"
                    data["code"] = 403
            except:
                if request.method == "POST":
                    Subscriptor.objects.create(
                        client=client,
                        account=account,
                        coupon_used="",
                    )
    except Exception, e:
        data["message"] = "the request is syntactically incorrect"
        data["code"] = 400

    return JsonResponse(data)
