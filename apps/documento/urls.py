from django.urls import path
from .views import UploadDocumento, DocumentoDelete

urlpatterns = [
]

htmx_ulrpatterns = [
    path('upload/<int:pk>/', UploadDocumento.as_view(), name='upload-documento'),
    path('delete/<int:pk>', DocumentoDelete.as_view(), name='delete-documento')
]

urlpatterns += htmx_ulrpatterns