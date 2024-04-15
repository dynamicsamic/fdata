import logging

from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from .models import Circuit
from .queries import get_circuits

logger = logging.getLogger(__name__)


def show_circuits(request: HttpRequest):
    theaders = Circuit.get_fieldnames()
    theaders.append("Num races")
    page_no = request.GET.get("page", 1)
    paginator = Paginator(get_circuits(), 15)
    page = paginator.get_page(page_no)

    return render(
        request,
        "stats/circuits.html",
        {"circuits": page, "theaders": theaders},
    )
