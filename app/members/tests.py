from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase


class AuthTokenTest(APITestCase):

    def test_auth_token(self):
        url = '/members/auth-token/'

        response = self.client.get(url)
        print(response)