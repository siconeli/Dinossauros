from django.urls import path
from .views import CadastroWizard

urlpatterns = [
    path('cadastro/', CadastroWizard.as_view(), name='cadastro_wizard'),
]