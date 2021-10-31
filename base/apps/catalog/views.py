from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import SAFE_METHODS
from .models import Brand
from .models import Product
from .models import ProductCounter
from .models import ProductTracker
from .serializers import BrandSerializer
from .serializers import ProductSerializer
from django.http import JsonResponse


class BrandViewSet(viewsets.ModelViewSet):
    """
    DETAIL, ACCESS ROL: ANONYMOUS, LIST ADD UPDATE DELETE, ACCESS ROL: ADMIN

    Brand of a product
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product, ACCES ROL: ADMIN

    A product should have basic info such as sku, name, price and brand
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]

    def retrieve(self, request, pk=None):
        """
        DETAIL GET, ACCESS ROL: ANONYMOUS

        Count visits by anonymous user
        """
        if request.method in SAFE_METHODS:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return JsonResponse({"detail": "Not found."}, status=404)
            try:
                product_counter = ProductCounter.objects.get(product=product)
                product_counter.counter = product_counter.counter + 1
                product_counter.save()
            except ProductCounter.DoesNotExist:
                p = ProductCounter(product=product, counter=1)
                p.save()
            finally:
                serializer = ProductSerializer(product)
                return JsonResponse(serializer.data, status=200)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def tracker(self, request, pk=None):
        """
        Track visits, ACCESS ROL: ANONYMOUS

        Track visits by anonymous user
        """

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)
        try:
            p = ProductTracker(product=product, useragent=request.headers)
            p.save()
        finally:
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data, status=200)
