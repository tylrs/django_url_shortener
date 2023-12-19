from django.test import TestCase
from .models import Url
from django.urls import reverse
import hashlib

class ShrinkifyViewTests(TestCase):
    def test_successful_shrinkify(self):
        """
        If the URL can be shrinkified correctly, it should redirect
        """

        params = {"shrinkify": "https://example.com"}
        response = self.client.post(reverse("byteaq:shrinkify"), params, follow=True)
        url = Url.objects.first()

        self.assertRedirects(response, 
                             reverse("byteaq:shrinkify_results", args=(1,)), 
                             status_code=302)
        self.assertTemplateUsed(response, template_name="byteaq/shrinkify_results.html")
        self.assertEqual(response.context["url"], url)

    def test_duplicate_successful_shrinkify(self):
        """
        If the URL has already been shrinkified, it can be shrinkified again and will return a different short url
        """
        long_url = "https://example.com"
        hash_object = hashlib.new("shake_256")
        hash_object.update(long_url.encode("UTF-8"))
        hashed_string = hash_object.hexdigest(4)
        url = Url.objects.create(
            short_url=f"https://byteaq.com/{hashed_string}",
            long_url=long_url
        )
    
        params = {"shrinkify": long_url}
        response = self.client.post(reverse("byteaq:shrinkify"), params, follow=True)
    
        self.assertEqual(response.context["url"].long_url, url.long_url)
        self.assertNotEqual(response.context["url"].short_url, url.short_url)




class ExpandViewTests(TestCase):
    def test_no_matching_short_url(self):
        """
        If no matching short url is found it should return 404
        """
        url = reverse("byteaq:expand")
        params = {"expand": "https://byteaq.com/c002169"}
        response = self.client.get(url, params)
        
        self.assertEqual(response.status_code, 404)

    def test_matching_short_url(self):
        """
        If a matching short url is found it should return the matching url
        """
        url = Url.objects.create(
            short_url="https://byteaq.com/c002178",
            long_url="https://example.com"
        )
        params = {"expand": "https://byteaq.com/c002178"}
        response = self.client.get(reverse("byteaq:expand"), params)

        self.assertEqual(response.context["url"], url)
        self.assertTemplateUsed(response, template_name="byteaq/expand_results.html")