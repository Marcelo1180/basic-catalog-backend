from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token as AuthToken


class Token(AuthToken):
    pass
    # key = models.CharField("Key", max_length=40, db_index=True, unique=True)
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     related_name="auth_token",
    #     on_delete=models.CASCADE,
    #     verbose_name="User",
    # )
