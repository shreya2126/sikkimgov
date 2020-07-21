from django.contrib.auth import get_user_model
from phone_verify.models import SMSVerification
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


# `send_phone_verify_email` function will get fired when a new entry is created or the model instance is updated
@receiver(post_save, sender=SMSVerification)
def send_phone_verify_email(sender, instance=None, created=None, **kwargs):
    # Check if the instance is created or not
    if created:
        send_mail(
            subject='Subject here',
            message='Here is the message.',
            from_email='from@example.com',
            recipient_list=['to@example.com'],
            fail_silently=False,
        )

def create_user_account(username, email, password, **extra_args):
    user = get_user_model().objects.create_user(
        username=username, email=email, password=password, **extra_args
    )
    ...
    return user