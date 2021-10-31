from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Brand


class TestCaseToken(APITestCase):
    fixtures = [
        "base/apps/catalog/tests/fixtures/auth_users.json",
        "base/apps/catalog/tests/fixtures/catalog.json",
    ]

    def setUp(self):
        self.client = Client()
        # Issue auth login successfully
        body = {"username": "admin", "password": "Developer"}
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Get Token
        self.token = response.json()["key"]

    def test_brand_success_list(self):
        # Issue
        response = self.client.get(
            "/catalog/v1/brand/",
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_brand_success_create(self):
        body = {"name": "Luuna"}
        # Issue
        response = self.client.post(
            "/catalog/v1/brand/",
            body,
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brand.objects.count(), 3)

    def test_brand_success_put(self):
        body = {"name": "Demo"}
        # Issue
        response = self.client.put(
            "/catalog/v1/brand/1/",
            body,
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Brand.objects.get(pk=1).name, "Demo")

    def test_brand_success_delete(self):
        # Issue
        response = self.client.delete(
            "/catalog/v1/brand/2/",
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Brand.objects.count(), 1)

    def test_brand_bad_brand(self):
        body = {"name": ""}
        # Issue
        response = self.client.post(
            "/catalog/v1/brand/",
            body,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, b'{"name":["This field may not be blank."]}')
