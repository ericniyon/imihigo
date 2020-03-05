from django.urls import path, include
from .views import generate_report,created_report

urlpatterns = [
    path('', generate_report, name='reporting'),
    path('reports/',created_report, name='created_report')
]