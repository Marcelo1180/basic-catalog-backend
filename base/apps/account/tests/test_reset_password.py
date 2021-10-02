import re
from urllib.parse import unquote
from django.test import TestCase, Client
from django.core import mail
from rest_framework import status
from rest_framework.test import APITestCase


class TestCasePassword(APITestCase):
    fixtures = ["base/apps/account/tests/fixtures/auth_users.json"]

    def setUp(self):
        self.client = Client()
        # Issue post password reset
        body = {"email": "jarteaga@demo.bo"}
        response = self.client.post("/account/v1/password/reset/", body)
        link_reset = re.search(
            "http://(.+?)/password_reset_link/(.+?)/(.+?)/", mail.outbox[0].body
        )
        self.url_reset = link_reset.group(0)
        self.uid = link_reset.group(2)
        self.token = link_reset.group(3)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_success_confirm_reset_password(self):
        # If exist the email in DB then send email
        # Issue
        body = {
            "uid": self.uid,
            "token": self.token,
            "new_password1": "NuevoPass",
            "new_password2": "NuevoPass",
        }
        response = self.client.post("/account/v1/password/reset/confirm/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if key result exist
        self.assertIn("detail", response.json())

    def test_success_redirect_link_reset_password(self):
        # If exist the email in DB then send email
        # Issue
        response = self.client.get(self.url_reset)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
