import time
import datetime
from django.test import TestCase, Client, override_settings
from rest_framework import status
from rest_framework.test import APITestCase


class TestCaseToken(APITestCase):
    fixtures = ["base/apps/account/tests/fixtures/auth_users.json"]

    def setUp(self):
        self.client = Client()
        # Issue auth login successfully
        body = {"username": "jarteaga", "password": "Developer"}
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Get Token
        self.token = response.json()["key"]

    @override_settings(TOKEN_TTL=datetime.timedelta(milliseconds=1))
    def test_get_user_expiration_tokend(self):
        # Forcing expiration token 1 ms and waitng 2 ms
        time.sleep(0.002)
        # Issue
        response = self.client.get(
            "/account/v1/user/", HTTP_AUTHORIZATION=f"Token {self.token}"
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Check if key result exist
        self.assertIn("error", response.json())
