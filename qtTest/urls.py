from django.contrib import admin
from django.urls import include, path
# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#from django.contrib.staticfiles.urls import staticfiles_urlpatternsc
schema_view = get_schema_view(
    openapi.Info(
        title="qt Test API",
        default_version='v1',
        description="Welcome to QT Test API documentation - qt Test",
       
        contact=openapi.Contact(email="rukundojanvier250@gmail.com"),
        license=openapi.License(name="MIT License - qt Test"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# drf_yasg code ends here

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('task', include('task.urls')),
   
]
#urlpatterns += staticfiles_urlpatterns()