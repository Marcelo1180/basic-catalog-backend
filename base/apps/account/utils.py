import pytz
from django.utils import timezone


def custom_create_token(token_model, user, serializer):
    utc_now = timezone.now()
    utc_now = utc_now.replace(tzinfo=pytz.utc)
    obj, created = token_model.objects.update_or_create(
        user=user,
        defaults={"created": utc_now},
    )
    return obj
