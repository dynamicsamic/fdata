from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render

from .models import Circuit


def show_circuits(request: HttpRequest):
    qs = Circuit.objects.annotate(num_races=Count("races"))
    theaders = Circuit.get_fieldnames()
    theaders.append("num_races")

    return render(
        request,
        "stats/circuits.html",
        {"circuits": qs, "theaders": theaders},
    )
