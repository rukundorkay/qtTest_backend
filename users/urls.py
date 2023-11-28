from django.urls import path
from .views import CustomLoginView,VerifyEmailByOTP, RegisterView,ForgotPasswordView,ResetPasswordView



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('verify-email/', VerifyEmailByOTP.as_view(), name='verify-email'),
    path('register/',  RegisterView.as_view(), name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    
]
