from django.http import HttpRequest
from django.shortcuts import render


async def index(request: HttpRequest):

    return render(request, "index.html")
