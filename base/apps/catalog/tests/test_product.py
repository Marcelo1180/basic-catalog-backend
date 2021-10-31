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
        # Issue auth login successfully
        body = {"username": "admin", "password": "Developer"}
        response = self.client.post("/account/v1/login/", body)
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Get Token
        self.token = response.json()["key"]

    def test_product_success_list(self):
        # Issue
        response = self.client.get(
            "/catalog/v1/product/",
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_success_detail(self):
        # Issue
        response = self.client.get(
            "/catalog/v1/product/1/",
            HTTP_AUTHORIZATION=f"Token {self.token}",
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
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 7)

    def test_product_success_patch(self):
        body = {"name": "Demo"}
        # Issue
        response = self.client.patch(
            "/catalog/v1/product/1/",
            body,
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(pk=1).name, "Demo")

    def test_product_success_delete(self):
        # Issue
        response = self.client.delete(
            "/catalog/v1/product/3/",
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        # Check status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 5)

    def test_product_bad_product(self):
        body = {"bad_field": ""}
        # Issue
        response = self.client.post(
            "/catalog/v1/product/",
            body,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content,
            b'{"sku":["This field is required."],"name":["This field is required."],"price":["This field is required."],"brand":["This field is required."]}',
        )
