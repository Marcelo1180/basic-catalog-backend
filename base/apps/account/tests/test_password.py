from django.test import TestCase, Client
from django.core import mail
from rest_framework import status
from rest_framework.test import APITestCase


class TestCasePassword(APITestCase):
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

    def test_success_change_password(self):
        # Issue
        body = {
            "new_password1": "Developer123",
            "new_password2": "Developer123",
            "old_password": "Developer",
        }
        response = self.client.post(
            "/account/v1/password/change/",
            body,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if key result exist
        self.assertIn("detail", response.json())

    def test_change_password_without_password2(self):
        # Issue
        body = {
            "new_password1": "Developer123",
            "old_password": "Developer",
        }
        response = self.client.post(
            "/account/v1/password/change/",
            body,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check if key result exist
        self.assertIn("new_password2", response.json())

    def test_change_password_without_old_password(self):
        # Issue
        body = {
            "new_password1": "Developer123",
            "new_password2": "Developer123",
        }
        response = self.client.post(
            "/account/v1/password/change/",
            body,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check if key result exist
        self.assertIn("old_password", response.json())

    def test_success_reset_password(self):
        # If exist the email in DB then send email
        # Issue
        # https://timonweb.com/django/testing-emails-in-django/
        body = {"email": "jarteaga@demo.bo"}
        response = self.client.post("/account/v1/password/reset/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check assert
        self.assertEqual(1, len(mail.outbox))
        self.assertEqual("jarteaga@demo.bo", mail.outbox[0].to[0])
        # Check if key result exist
        self.assertIn("detail", response.json())

    def test_reset_password_bad_email(self):
        # If don't exist the email in DB then not send email
        # Issue
        body = {"email": "emailnotexist@demo.bo"}
        response = self.client.post("/account/v1/password/reset/", body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check assert
        self.assertEqual(0, len(mail.outbox))
        # Check if key result exist
        self.assertIn("detail", response.json())
