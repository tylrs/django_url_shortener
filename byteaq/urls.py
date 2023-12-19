from django.urls import path

from . import views

app_name="byteaq"

urlpatterns = [
    path("", views.index, name="index"),
    path("shrinkify/", views.shrinkify, name="shrinkify"),
    path("shrinkify/results/<int:url_id>/", views.shrinkify_results, name="shrinkify_results"),
    path("expand/", views.expand, name="expand"),
]