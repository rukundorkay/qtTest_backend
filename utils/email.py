import os
import random
from django.conf import settings
from django.core.mail import send_mail
from users.models import CustomUser as User, VerifyEmail, ResetPassword

def generate_otp():
    return str(random.randint(100000, 999999))

def send_welcome_email(user_email):
    
    otp = generate_otp()
    subject = 'Welcome to Task managment software.'
    message = f'Thank you for registering . We hope you will enjoy! using task manager'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    # saving otp to related user
    user_obj = User.objects.get(email=user_email)
    
    if user_obj is not None:
        VerifyEmail.objects.create(
            email=user_email,
            otp=otp
        )

def send_reset_password_email(user_email):
    code = generate_otp()
    subject = 'Reset Password Instructions '
    message = f'You forgot your password, don\'t worry we got you covered, Please verify using this Code to reset your password: {code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    # saving code to related user
    user_obj = User.objects.get(email=user_email)
    if user_obj is not None:
        ResetPassword.objects.create(
            email=user_email,
            code=code
        )


