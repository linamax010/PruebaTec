from django.urls import path
from .views import IngresoOperacion, OperacionView, OperacionDel


urlpatterns = [
    path('multiplicar/', IngresoOperacion.as_view(), name='ingreso_operacion'),
    path('multiplicar/consulta/', OperacionView.as_view(), name='envio_resultado'),
    path('multiplicar/eliminar/', OperacionDel.as_view(), name='eliminar_datos'),
]