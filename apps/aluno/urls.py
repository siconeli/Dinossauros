from django.urls import path
from .views import AlunoDetail, AlunoUpdate, AlunoDelete

urlpatterns = [
    path('detail/<int:pk>/', AlunoDetail.as_view(), name='aluno-detail'),
    path('delete/<int:pk>/', AlunoDelete.as_view(), name='aluno-delete')
]

htmx_urlpatterns = [
    path('update/<int:pk>/', AlunoUpdate.as_view(), name='aluno-update'),
]

urlpatterns += htmx_urlpatterns