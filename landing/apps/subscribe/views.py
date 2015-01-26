import requests
import json
from django.shortcuts import render
from django.http import JsonResponse


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
    except Exception, e:
        data["message"] = "the request is syntactically incorrect"
        data["code"] = 400

    return JsonResponse(data)
