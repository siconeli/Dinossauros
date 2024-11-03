from django.urls import path
from .views import ResponsavelCreate, ResponsavelUpdate, ResponsavelDelete

urlpatterns = [
    path('create/<int:pk>/', ResponsavelCreate.as_view(), name='resp-create'),
    path('update/<int:pk>/', ResponsavelUpdate.as_view(), name='resp-update'),
    path('delete/<int:pk>/', ResponsavelDelete.as_view(), name='resp-delete')
]