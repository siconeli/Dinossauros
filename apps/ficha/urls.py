from django.urls import path
from .views import FichaUpdate

urlpatterns = [

]

htmx_urlpatterns = [
    path('update/<int:pk>', FichaUpdate.as_view(), name='ficha-update')
]

urlpatterns += htmx_urlpatterns