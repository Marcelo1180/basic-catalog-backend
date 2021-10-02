from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase


class TestCaseLogin(APITestCase):
    fixtures = ["base/apps/account/tests/fixtures/auth_users.json"]

    def setUp(self):
        self.client = Client()

    def test_login_success_username(self):
        # Issue auth login successfully
        body = {"username": "jarteaga", "password": "Developer"}
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if key result exist
        self.assertIn("key", response.json())

    def test_login_success_email(self):
        # Issue auth login successfully
        body = {"email": "jarteaga@demo.bo", "password": "Developer"}
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if key result exist
        self.assertIn("key", response.json())

    def test_login_success_email_bad_username(self):
        # Issue auth login successfully
        body = {
            "email": "jarteaga@demo.bo",
            "username": "baduser",
            "password": "Developer",
        }
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if key result exist
        self.assertIn("key", response.json())

    def test_login_success_username_bad_email(self):
        # Issue auth login successfully
        body = {
            "username": "jarteaga",
            "email": "bademail@demo.bo",
            "password": "Developer",
        }
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if key result exist
        self.assertIn("key", response.json())

    def test_login_bad_username(self):
        body = {"username": "noexiste", "password": "Developer"}
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check if non_field_errors result exist
        self.assertIn("non_field_errors", response.json())

    def test_login_bad_email(self):
        # Issue auth login successfully
        body = {"email": "jarteaga1@demo.bo", "password": "Developer"}
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check if non_field_errors result exist
        self.assertIn("non_field_errors", response.json())

    def test_login_only_password(self):
        body = {"password": "Developer"}
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check if non_field_errors result exist
        self.assertIn("non_field_errors", response.json())
