from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from apps.formWizard.forms import ContratoForm
from .models import Contrato
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class ContratoUpdate(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            contrato = get_object_or_404(Contrato, pk=pk)
            form = ContratoForm(request.POST, instance=contrato)

            if form.is_valid():
                form.save()
                return render(request,'fragmento/contrato_update.html', {'contrato':contrato})
        
            return render(request, 'fragmento/contrato_update.html', {'form':form, 'contrato':contrato})
            
        except Exception as e:
            print(f'ContratoUpdate -> {e}')
            return render(request, 'fragmento/contrato_update.html', {'form':form, 'contrato':contrato})