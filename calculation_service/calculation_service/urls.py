from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title='CalculationAPI')),
    path('schema/', get_schema_view(
            title='CalculationAPI',
            description='API for calculation operations',
            version='1.0.0'
        ), name='openapi-schema')
]
