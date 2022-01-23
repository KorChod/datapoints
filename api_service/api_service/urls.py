from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title='DataPointAPI')),
    path('schema/', get_schema_view(
        title='DataPointAPI',
        description='API for data-points details',
        version='1.0.0'
    ), name='openapi-schema')
]
