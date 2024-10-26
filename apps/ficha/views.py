from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from apps.formWizard.forms import FichaForm
from .models import Ficha

class FichaUpdate(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            ficha = get_object_or_404(Ficha, pk=pk)

            form = FichaForm(self.request.POST, instance=ficha)

            if form.is_valid():
                form.save()
              
                return render(request, 'fragmento/ficha_update.html', {'ficha':ficha})
            
            return render(request, 'fragmento/ficha_update.html', {'form':form, 'ficha':ficha})
        
        except Exception as e:
            print(f'FichaUpdate -> {e}')
