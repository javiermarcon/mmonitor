#from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Empresa, Maquina


def index(request):
    monitoring_list = Empresa.objects.order_by('-nombre') #[:5]
    context = {'monitoring_list': monitoring_list}
    return render(request, 'tor_monitoring/index.html', context)

def detalle(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    empresa.maquina_set.all()
    return render(request, 'tor_monitoring/detalle.html', {'empresa': empresa})
