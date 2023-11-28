from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser as User
from utils.email import send_welcome_email

@receiver(post_save, sender=User)
def send_welcome_email_on_user_creation(sender, instance, created, **kwargs):
    print('creatin user with signals')
    # Check if a new user is created and is not superuser
    if created and not instance.is_superuser:
        user_email = instance.email
        send_welcome_email(user_email)  # Send the welcome email
