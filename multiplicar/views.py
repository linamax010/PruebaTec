import json
#from django import views                         #Modulo Json
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from .models import Operacion          # Modelo estructura Base Datos
from django.http import JsonResponse   # Libreria para enviar formato Json
from django.http.response import JsonResponse   # Libreria para enviar formato Json
from django.utils.decorators import method_decorator # Metodo Para Utilizar Bypass CSRF
from django.views.decorators.csrf import csrf_exempt # Metodo Para Utilizar Bypass CSRF
from django.forms.models import model_to_dict



class IngresoOperacion(View):
    
    @method_decorator(csrf_exempt) # CSRF
    def dispatch(self, request, *args, **kwargs): # CSRF
        return super().dispatch(request, *args, **kwargs) # CSRF 
    
    def post(self, request):
        jd=json.loads(request.body)  # Modulo para pasar a Diccionario
        datos = Operacion.objects.create(
            num1=(jd['numero1']), num2=(jd['numero2']),
            resultado=(str((int(jd['numero1'])*int(jd['numero2']))))
            )
        #datos = {'resultado':'resultado'}
        return JsonResponse(model_to_dict(datos))


class OperacionView(View):
    @method_decorator(csrf_exempt) # CSRF
    def dispatch(self, request, *args, **kwargs): # CSRF
        return super().dispatch(request, *args, **kwargs) # CSRF
    
    # get
    def get(self, request):
        cList = Operacion.objects.all()
        return JsonResponse(list(cList.values()), safe=False) # Devolver un objeto tipo array con el off

"""
#Clase para Eliminar
class OperacionDel(View):
    @method_decorator(csrf_exempt) # CSRF
    def dispatch(self, request, *args, **kwargs): # CSRF
        return super().dispatch(request, *args, **kwargs) # CSRF
    
    def delete(self, request, pk):
        campos = list(Operacion.objects.filter(pk=pk))
        if len(campos) > 0:
            Operacion.objects.filter(pk=pk).delete()
            datos = {'message':'Success'}
        else:
            datos = {'message': "Campo no Existe..."}

        return JsonResponse(datos)
"""
class OperacionDel(View):
    @method_decorator(csrf_exempt) # CSRF
    def dispatch(self, request, *args, **kwargs): # CSRF
        return super().dispatch(request, *args, **kwargs) # CSRF
    
    def delete(self, request):
        campos = list(Operacion.objects.all())
        if len(campos) > 0:
            Operacion.objects.all().delete()
            datos = {'message':'Success'}
        else:
            datos = {'message': "No hay datos!"}

        return JsonResponse(datos)