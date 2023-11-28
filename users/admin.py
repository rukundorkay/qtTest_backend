from django.contrib import admin
from users.models import CustomUser, VerifyEmail, ResetPassword


admin.site.register(CustomUser)
admin.site.register(VerifyEmail)
admin.site.register(ResetPassword)
