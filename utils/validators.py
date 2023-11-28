from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

def validate_password_complexity(value):
    # Minimum 8 characters
    min_length_validator = MinLengthValidator(limit_value=8)
    min_length_validator(value)

    # Maximum 16 characters
    max_length_validator = MaxLengthValidator(limit_value=16)
    max_length_validator(value)

    # At least one digit
    if not any(char.isdigit() for char in value):
        raise ValidationError("The password must contain at least one digit (0-9).")

    # At least one letter
    if not any(char.isalpha() for char in value):
        raise ValidationError("The password must contain at least one letter (a-zA-Z).")


