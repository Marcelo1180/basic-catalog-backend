from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from base.apps.account.views import view_status
from django.conf.urls.static import static


urlpatterns = [
    path("", view_status),
    path("account/v1/", include("base.apps.account.urls")),
    path("catalog/v1/", include("base.apps.catalog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Show apidoc if DEBUG is activated
schema_view = get_schema_view(
    openapi.Info(
        title="Test Zebrands Backend",
        default_version="v0.0.1",
        description="Basic catalog system to manage products",
        terms_of_service="https://raw.githubusercontent.com/Marcelo1180/django-base-backend/main/LICENSE",
        contact=openapi.Contact(email="arteagamarcelo@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),
        url(
            r"^apidoc(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        url(
            r"^apidoc/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
