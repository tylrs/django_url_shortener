from django.db import models

class Url(models.Model):
    short_url = models.CharField(max_length=2000, unique=True)
    long_url = models.CharField(max_length=2000)

    def __str__(self):
        return f'short: {self.short_url} long: {self.long_url}'