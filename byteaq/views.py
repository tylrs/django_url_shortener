from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "byteaq/index.html")
    # return HttpResponse("Hello, world. You're at the byteaq index.")