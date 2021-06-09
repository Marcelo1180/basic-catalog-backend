from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase


class TestCaseUser(APITestCase):
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

    def test_success_get_user(self):
        # Issue
        response = self.client.get(
            "/account/v1/user/", HTTP_AUTHORIZATION=f"Token {self.token}"
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check assert
        self.assertEqual(2, response.json()["pk"])
        self.assertEqual("jarteaga", response.json()["username"])
        self.assertEqual("jarteaga@demo.bo", response.json()["email"])
        self.assertEqual("Juan Marcelo", response.json()["first_name"])
        self.assertEqual("Arteaga Gutierrez", response.json()["last_name"])

    def test_get_user_without_token(self):
        # Issue
        response = self.client.get("/account/v1/user/")
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Check if key result exist
        self.assertIn("detail", response.json())

    def test_get_user_after_logout(self):
        # Issue
        response = self.client.post(
            "/account/v1/logout/", HTTP_AUTHORIZATION=f"Token {self.token}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(
            "/account/v1/user/", HTTP_AUTHORIZATION=f"Token {self.token}"
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Check if key result exist
        self.assertIn("detail", response.json())
