from django.urls import path

from .views import CalculationView

urlpatterns = [
    path('aggregate-data/', CalculationView.as_view()),
]
