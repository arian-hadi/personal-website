from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', ContactView.as_view(), name = 'contact'),
    path('success/', SuccessView.as_view(), name = 'success')
]