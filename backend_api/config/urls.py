from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.decorators import login_required


schema_view = get_schema_view(
    openapi.Info(
        title='Rent car',
        default_version='v1',
    ), 
    public=False,
    permission_classes=[IsAdminUser],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema_swagger_ui'),
    path('', include('apps.car.urls')),
]
