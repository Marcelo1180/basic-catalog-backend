from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from base.apps.catalog import views
from django.urls import path


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
    url('filter/brand/(?P<id>[0-9]+)/product/$', views.filter_product),
    path('search/product/', views.search_product),
]

