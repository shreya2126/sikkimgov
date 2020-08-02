from django.test import TestCase
from rest_framework.test import APITestCase
from . serializers import intermediatorLoginSerializer
from sikkimgov.models import intermediatorLogin
import json
from django.contrib.auth.models import User
from django.urls import reverse

from .views import intermediatorLogin


from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


class intermediatorLoginTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('intermediatorLogin/', include('intermediatorLogin.urls')),
    ]

    def test_intermediatorLogin(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('intermediatorLogin')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)