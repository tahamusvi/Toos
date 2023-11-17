from django.contrib import admin
from django.urls import path,include
from .settings import admin_url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API Documentation for hotel",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="FivePlusOne.ir@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)





urlpatterns = [
    path(f'admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
