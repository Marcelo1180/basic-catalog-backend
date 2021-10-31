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

    def test_brand_success_list(self):
        # Issue
        response = self.client.get(
            "/catalog/v1/brand/",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_brand_success_detail(self):
        # Issue
        response = self.client.get(
            "/catalog/v1/brand/1/",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_brand_success_create(self):
        body = {"name": "Demo"}
        # Issue
        response = self.client.post(
            "/catalog/v1/brand/",
            body,
            content_type="application/json",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_brand_success_put(self):
        body = {"name": "Demo"}
        # Issue
        response = self.client.put(
            "/catalog/v1/brand/1/",
            body,
            content_type="application/json",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Brand.objects.get(pk=1).name, "rem")

    def test_brand_success_delete(self):
        # Issue
        response = self.client.delete(
            "/catalog/v1/brand/2/",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Brand.objects.count(), 2)

    def test_brand_bad_brand(self):
        body = {"name": ""}
        # Issue
        response = self.client.post(
            "/catalog/v1/brand/",
            body,
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.content,
            b'{"detail":"Authentication credentials were not provided."}',
        )
