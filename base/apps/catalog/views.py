from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.permissions import SAFE_METHODS
from rest_framework.decorators import api_view
from django.db.models import Q
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
                # Counter of products
                product_counter = ProductCounter.objects.get(product=product)
                product_counter.counter = product_counter.counter + 1
                product_counter.save()

                # Save user agent to tracking

                product_tracker = ProductTracker(product=product, useragent=request.headers)
                product_tracker.save()

            except ProductCounter.DoesNotExist:
                p = ProductCounter(product=product, counter=1)
                p.save()
            finally:
                serializer = ProductSerializer(product, context={"request": request})
                return JsonResponse(serializer.data, status=200)

@api_view(["GET"])
@permission_classes([AllowAny])
def search_product(request):
    """
    Search Products, ACCESS ROL: ANONYMOUS

    Search products by name and description => v1/product/search/?query=Algo a buscar
    """

    query = request.GET.get("query", "")
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = ProductSerializer(
            products, context={"request": request}, many=True
        )
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse({"products": []})


@api_view(["GET"])
@permission_classes([AllowAny])
def filter_product(request, id):
    """
    Filter by Brand, ACCESS ROL: ANONYMOUS

    Filter products by brand
    """
    products = Product.objects.filter(brand=id)
    serializer = ProductSerializer(products, context={"request": request}, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)
