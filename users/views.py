from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import CustomUser, VerifyEmail, ResetPassword
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status,generics
from rest_framework.exceptions import AuthenticationFailed
from utils.email import send_reset_password_email
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import authenticate
from users.authenticate import CustomModelBackend
from users.serializers import RegisterSerializer, UserSerializer, VerifyEmailByOTPSerializer,ResetPasswordSerializer


class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = CustomModelBackend.authenticate(self, request, username=username, password=password)

        if user is not None:
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                # Serialize the user data
                user_serializer = UserSerializer(user)

                response_data = {
                    'token': token.key,
                    'user': user_serializer.data,
                }
                return Response({
                'code':status.HTTP_200_OK,
                'data':response_data
            }, status=status.HTTP_200_OK)
             
            return Response({
                'error': 'Unable to log in with provided credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({
                'error': 'Unable to log in with provided credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
class VerifyEmailByOTP(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'otp': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: 'Email verified successfully!',
            400: 'Invalid OTP',
            500: 'Internal server error',
        }
    )

    def post(self, request):
        try:
            data = request.data
            serializer = VerifyEmailByOTPSerializer(data= data)

            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                # Find the user_verify instance
                user_verify = VerifyEmail.objects.filter(email=email, otp=otp).first()

                if user_verify:
                    # Update the user's is_active field to True
                    user = CustomUser.objects.get(email=email)
                    user.is_active = True
                    user.save()

                    # Delete the user_verify instance
                    user_verify.delete()

                    return Response({
                        'status': status.HTTP_200_OK,
                        'message': 'Email verification successful. Your account is now active.',
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'Invalid OTP. Please check your OTP and try again.',
                    }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Error occured',
                'data': serializer.error
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
         
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Internal Server Error',
                'data': None
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
# Create your views here.
class RegisterView(generics.CreateAPIView):
    """
        This is used to register user.
    """
    serializer_class = RegisterSerializer
    
    def get_queryset(self):
        return CustomUser.objects.first()
    
class ForgotPasswordView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: 'Password reset instructions sent to Email',
            400: 'Invalid Email or Code',
            404: 'User not found',
        }
    )

    def post(self, request):
        try:
            email = request.data.get('email')

            try:
                user = CustomUser.objects.get(email=email)
            except ObjectDoesNotExist:
                # User with the provided email does not exist
                return Response({
                    'status': status.HTTP_404_NOT_FOUND,
                    'message': 'User with this email does not exist.',
                }, status=status.HTTP_404_NOT_FOUND)

            # Send reset password instructions to the user's email
            send_reset_password_email(user.email)

            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Reset password instructions sent to your email. Please check your email!',
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Internal Server Error',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ResetPasswordView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING),
                'new_password': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: 'Password updated successfully',
            400: 'Invalid Email or Code',
        }
    )
    
    def post(self, request):
        try:
            data = request.data
            serializer = ResetPasswordSerializer(data= data)

            if serializer.is_valid():
                email = serializer.data['email']
                code = serializer.data['code']
                # new_password = serializer.data['new_password']

                # updating user password  logics here
                user_reset = ResetPassword.objects.filter(email = email, code =code).first()
                if user_reset:
                    # Update user password to new password
                    new_password = data.get('new_password')

                    user = CustomUser.objects.get(email= email)
                    user.set_password(new_password)
                    user.save()

                    # Delete user_reset instace
                    user_reset.delete()

                    return Response({
                    'status': 200,
                    'message': 'Password updated successfully',
                }, status=status.HTTP_200_OK)

                else:
                    return Response({
                        'status': 400,
                        'message': 'Invalid Email or Code. Please check your email or code and try again.',
                    }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'status': 400,
                'message': 'Error occured',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': None
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )