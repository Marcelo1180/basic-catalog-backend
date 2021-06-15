from django.urls import path, re_path, include
from django.views.generic import TemplateView
from base.apps.account import views


urlpatterns = [
    path("status", views.view_status),
    path("", include("dj_rest_auth.urls")),
    # Path used to redirect or complete the form
    path(
        "password_reset_link/<uidb64>/<token>/",
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
]
