from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Url
import hashlib

def index(request):
    return render(request, "byteaq/index.html")

def shrinkify(request):
    print(f'REQUEST {request.POST["shrinkify"]}')
    url = request.POST["shrinkify"]
    hash_object = hashlib.new("shake_256")
    hash_object.update(url.encode("UTF-8"))
    hashed_string = hash_object.hexdigest(4)
    u, created = Url.objects.get_or_create(
        short_url=f"http://byteaq.com/{hashed_string}", 
        defaults={
            "long_url": url
        }
    )

    if created:
        print(f"Object with name '{hashed_string}' was created.")
    else:
        print(f"Object with name '{u}' already exists.")
    
    print(f'url:{url} HASHED STRING: {hashed_string} created: {created}')
    return HttpResponse(hashed_string)

def expand(request):
    return HttpResponse("Hello, world. You're at expand")