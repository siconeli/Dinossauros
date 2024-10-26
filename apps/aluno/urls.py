from django.urls import path
from .views import AlunoDetail, AlunoUpdate

urlpatterns = [
    path('detail/<int:pk>/', AlunoDetail.as_view(), name='aluno-detail'),
]

htmx_urlpatterns = [
    path('update/<int:pk>/', AlunoUpdate.as_view(), name='aluno-update'),
]

urlpatterns += htmx_urlpatterns