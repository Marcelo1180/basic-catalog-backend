from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template
from django.conf import settings
from .models import Product


@receiver(post_save, sender=Product)
def post_save_product(sender, instance, **kwargs):
    """
    Notify all other admins about the change, either via email or other mechanism.
    """
    # Find staff users's emails
    to_users = [user.email for user in User.objects.filter(is_staff=True) if user.email]

    # Send email to users
    body_plain = get_template('email.txt')
    body_html = get_template('email.html')
    context = {
        'sku': instance.sku,
        'name': instance.name,
        'price': instance.price,
        'brand': instance.brand,
        'sender': settings.DEFAULT_FROM_EMAIL,
    }
    
    send_mail(
        'Product has changed',
        body_plain.render(context),
        settings.DEFAULT_FROM_EMAIL,
        to_users,
        html_message=body_html.render(context),
        fail_silently=False,
    )
