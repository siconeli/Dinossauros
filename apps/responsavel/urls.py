from django.urls import path
from .views import ResponsavelCreate, ResponsavelDelete

urlpatterns = [
    path('create/<int:pk>/', ResponsavelCreate.as_view(), name='resp-create'),
    path('delete/<int:pk>/', ResponsavelDelete.as_view(), name='resp-delete')
]