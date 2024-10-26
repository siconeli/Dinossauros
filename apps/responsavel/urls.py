from django.urls import path
from .views import ResponsavelCreate

urlpatterns = [
    path('create/<int:pk>/', ResponsavelCreate.as_view(), name='resp-create'),
]