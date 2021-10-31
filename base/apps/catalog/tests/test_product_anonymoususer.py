from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Product
from ..models import ProductCounter
from ..models import ProductTracker


class TestCaseToken(APITestCase):
    fixtures = [
        "base/apps/catalog/tests/fixtures/auth_users.json",
        "base/apps/catalog/tests/fixtures/catalog.json",
    ]

    def setUp(self):
        self.client = Client()

    def test_product_success_list(self):
        # Issue
        response = self.client.get(
            "/catalog/v1/product/",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_success_detail(self):
        # Issue
        response = self.client.get(
            "/catalog/v1/product/1/",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductCounter.objects.count(), 1)

    def test_product_success_detail_tracker(self):
        # Issue
        response = self.client.get(
            "/catalog/v1/product/1/tracker/",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductTracker.objects.count(), 1)

    def test_product_success_create(self):
        body = {
            "sku": "DE1001",
            "name": "Product demo1",
            "price": "123.99",
            "brand": 1,
        }
        # Issue
        response = self.client.post(
            "/catalog/v1/product/",
            body,
            content_type="application/json",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_product_success_put(self):
        body = {"name": "Demo"}
        # Issue
        response = self.client.put(
            "/catalog/v1/product/1/",
            body,
            content_type="application/json",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Product.objects.get(pk=1).name, "Almohada Ajustable")

    def test_product_success_delete(self):
        # Issue
        response = self.client.delete(
            "/catalog/v1/product/2/",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Product.objects.count(), 6)

    def test_product_bad_product(self):
        body = {"name": ""}
        # Issue
        response = self.client.post(
            "/catalog/v1/product/",
            body,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.content,
            b'{"detail":"Authentication credentials were not provided."}',
        )
