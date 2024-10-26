from django.urls import path
from .views import ContratoUpdate

urlpatterns = [
    
]

htmx_urlpatterns = [
    path('update/<int:pk>/', ContratoUpdate.as_view(), name='contrato-update')
]

urlpatterns += htmx_urlpatterns