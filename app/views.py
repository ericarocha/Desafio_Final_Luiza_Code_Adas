from django.shortcuts import render
from app.models import Segmentos
from app.forms import Segmentos_form
from django.http import HttpResponseRedirect

'''
Funções para renderização do template
'''
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {'form':Segmentos_form()}
    return render(request, 'form.html', data, create)

def create(request):
    form = Segmentos_form(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("./")

