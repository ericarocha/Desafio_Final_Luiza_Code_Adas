from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from app.models import Segmentos, Empresas, Produtos
from app.forms import SegmentosForm, EmpresasForm, ProdutosForm
from django.http import HttpResponseRedirect


'''
Funções para renderização do template
'''
def home(request):
    return render(request, 'front.html')

def form(request):
    data = {'form': SegmentosForm()}
    return render(request, 'form.html', data)

def cd_empresa(request):
    dataemp = {'cdempresa': EmpresasForm()}
    return render(request, 'cd_empresa.html', dataemp)

def cd_produto(request):
    dataprod = {'cdproduto': ProdutosForm()}
    return render(request, 'cd_produto.html', dataprod)


def create(request):
    form = SegmentosForm(request.POST or None)
    if form.is_valid(): 
        form.save()
    return HttpResponseRedirect ("/")

def create2(request):    
    cd_empresa = EmpresasForm(request.POST or None)
    if cd_empresa.is_valid(): 
        cd_empresa.save()
    return HttpResponseRedirect ("/")

def createprod(request):
    cd_produto = ProdutosForm(request.POST or None)
    if cd_produto.is_valid(): 
        cd_produto.save()
    return HttpResponseRedirect ("/")

