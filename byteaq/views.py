from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Url
import hashlib
import random

def index(request):
    return render(request, "byteaq/index.html")

def shrinkify(request):
    url = request.POST["shrinkify"]
    hash_object = hashlib.new("shake_256")
    hash_object.update(url.encode("UTF-8"))
    hashed_string = hash_object.hexdigest(4)

    u, created = Url.objects.get_or_create(
        short_url=f"https://byteaq.com/{hashed_string}", 
        defaults={
            "long_url": url
        }
    )
    
    while not created:
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        random_char = random.choice(characters)
        hashed_string += random_char

        u, created = Url.objects.get_or_create(
            short_url=f"https://byteaq.com/{hashed_string}", 
            defaults={
                "long_url": url
            }
        )
        
    return HttpResponseRedirect(reverse("byteaq:shrinkify_results", args=(u.id,)))

def shrinkify_results(request, url_id):
    url = get_object_or_404(Url, id=url_id)
    context = {"url": url}
    
    return render(request, "byteaq/shrinkify_results.html", context)


def expand(request):
    short_url = request.GET["expand"]
    url = get_object_or_404(Url, short_url=short_url)
    context = {"url": url}

    return render(request, "byteaq/expand_results.html", context)