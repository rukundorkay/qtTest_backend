from rest_framework import serializers
from django.core.exceptions import ValidationError
from utils.validators import validate_password_complexity
from .models import CustomUser, VerifyEmail
from utils.email import generate_otp, send_welcome_email

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "gender",
            "email",
            "phone_number",
            "is_active",
            "is_superuser"
        )

        read_only_fields = fields

class VerifyEmailByOTPSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

    class Meta:
        model = VerifyEmail
        fields = [
            'email',
            'otp'
        ]

class RegisterSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(write_only=True, validators=[validate_password_complexity])
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'first_name', 
            'last_name', 
            'email', 
            'password', 
            'phone_number', 
            'gender', 
           
        )

    def create(self, validated_data):
        password = validated_data.get('password')
        user = CustomUser.objects.create(**validated_data)
        # hash password
        user.set_password(password)
        user.save()
        if user is not None:
            VerifyEmail.objects.create(
                email=validated_data['email'],
                otp=generate_otp()
        )
        return user
    
class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    code = serializers.CharField()
    new_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = VerifyEmail
        fields = [
            'email',
            'code',
            'new_password'
        ]
    
    def validate(self, data):
        # Check if the required fields are present in the data
        required_fields = ['email', 'code', 'new_password']

        for field in required_fields:
            if field not in data:
                raise ValidationError({field: ['This field is required.']})

        return data




