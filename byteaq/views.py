from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Url
import hashlib
import random

def index(request):
    return render(request, "byteaq/index.html")

def shrinkify(request):
    # print(f'1) REQUEST {request.POST["shrinkify"]}')
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
        # print(f"2) Object with name '{hashed_string}' already exists.")
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        random_char = random.choice(characters)
        hashed_string += random_char

        u, created = Url.objects.get_or_create(
            short_url=f"https://byteaq.com/{hashed_string}", 
            defaults={
                "long_url": url
            }
        )
        # print(f'End of loop {u} {created}')
        
    
    print(f'url:{url} HASHED STRING: {hashed_string} created: {created}')
    print(f'LOOK HERE>>> {u} {u.id}')
    # print(f'{reverse("byteaq:shrinkify_results", args=(u.id))}')
    return HttpResponseRedirect(reverse("byteaq:shrinkify_results", args=(u.id,)))

def shrinkify_results(request, url_id):
    url = get_object_or_404(Url, id=url_id)
    context = {"url": url}
    return render(request, "byteaq/shrinkify_results.html", context)


def expand(request):
    print(f'1) REQUEST {request.GET["expand"]}')
    short_url = request.GET["expand"]
    url = get_object_or_404(Url, short_url=short_url)
    print(f'Expand results {url}')

    # return HttpResponse(f'Look at url info here: {url}')
    context = {"url": url}
    return render(request, "byteaq/expand_results.html", context)