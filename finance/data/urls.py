from django.urls import path
from . import views

urlpatterns = [
    path('inflation-overview/', views.inflation_overview, name='inflation_overview'),
]
