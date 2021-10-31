from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def send_mail_template():
    templatex = "email.html"
    plaintext = get_template(templatex)
    htmly = get_template(templatex)

    d = Context({"username": "hola"})

    subject, from_email, to = "hello", "from@example.com", "to@example.com"
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
