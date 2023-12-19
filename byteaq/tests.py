from django.test import TestCase
from .models import Url
from django.urls import reverse

class ExpandViewTests(TestCase):
    def test_no_matching_short_url(self):
        """
        If no matching short url is found it should return 404
        """
        url = reverse("byteaq:expand")
        params = {"expand": "https://byteaq.com/c002178"}
        print(f'LOOK AT URL>> {url} PARAMS: {params}')
        response = self.client.get(url, params)
        print(f'RESPONSE>>>{response}')
        self.assertEqual(response.status_code, 404)
        # self.assertContains(response, "No polls are available.")
        # self.assertQuerySetEqual(response.context["latest_question_list"], [])

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
        self.assertContains(response, "c002178")
        # self.assertQuerySetEqual(
        #     response.context["latest_question_list"],
        #     [url],
        # )
