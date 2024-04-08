from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render

from .models import Circuit


async def get_circuits():
    return Circuit.objects.annotate(num_races=Count("races")).order_by(
        "-num_races"
    )


async def show_circuits(request: HttpRequest):
    qs = await get_circuits()
    theaders = Circuit.get_fieldnames()
    theaders.append("num_races")

    return render(
        request,
        "stats/circuits.html",
        {"circuits": qs, "theaders": theaders},
    )
