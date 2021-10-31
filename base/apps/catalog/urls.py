from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from base.apps.catalog import views


router = DefaultRouter()
"""
Brand
"""
router.register(r"brand", views.BrandViewSet)

"""
Product
"""
router.register(r"product", views.ProductViewSet)


urlpatterns = [
    url("", include(router.urls)),
]

