from django import views
from django.urls import path
from .views import UploadDocumento

urlpatterns = [
    
]

htmx_ulrpatterns = [
    path('upload/<int:pk>/', UploadDocumento.as_view(), name='upload-documento')
]

urlpatterns += htmx_ulrpatterns