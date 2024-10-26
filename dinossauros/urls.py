from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('central-admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('apps.core.urls')),
    path('aluno/', include('apps.aluno.urls')),
    path('responsavel/', include('apps.responsavel.urls')),
    path('contrato/', include('apps.contrato.urls')),
    path('ficha/', include('apps.ficha.urls')),
    path('forms/aluno/', include('apps.formWizard.urls')),
    path('documento/', include('apps.documento.urls')),
]

if settings.DEBUG: 
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_URL)

admin.site.site_title = 'Cadastros' 
admin.site.site_header = 'Central Administrativa' 
admin.site.index_title = 'Cadastros'