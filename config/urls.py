from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('users.urls'))
]

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="test API",
        default_version='v1',
        description="Swagger API 문서",
        contact=openapi.Contact(email="diqkqkqk@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    validators=['flex', 'ssv'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
	# drf API docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]