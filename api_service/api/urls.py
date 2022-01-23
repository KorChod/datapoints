from django.urls import path

from .views import DataPointList, ApiStatusView, DataPointQuery

urlpatterns = [
    path('', DataPointList.as_view()),
    path('<str:datapoint_name>/', DataPointQuery.as_view()),
    path('check-api-status/', ApiStatusView.as_view())
]
