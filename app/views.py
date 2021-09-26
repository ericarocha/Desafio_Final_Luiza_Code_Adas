from django.http.response import HttpResponse, HttpResponseRedirect, ResponseHeaders
from django.shortcuts import redirect, render
from app.models import Segmentos, Empresas, Produtos
from app.forms import SegmentosForm, EmpresasForm, ProdutosForm
from django.http import HttpResponseRedirect


'''
Funções para renderização do template
'''
def home(request):
    data = {}
    data ['db'] = Segmentos.objects.all()  
    data ["dbe"] = Empresas.objects.all()
    data ["dbp"] = Produtos.objects.all()
    return render(request, 'front.html', data)
    

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

def viewseg (request, pk):
    dataseg = {'db': Segmentos.object.get(pk=pk)}
    return render (request, 'viewseg.html', dataseg)

def editseg(request, pk):
    dataseg = {}
    dataseg['db'] = Segmentos.objects.get(pk=pk)
    dataseg['form'] = SegmentosForm(instance=dataseg['db'])
    return render(request, 'form.html', dataseg)

def editemp(request, pk):
    dataemp = {}
    dataemp['db'] = Empresas.objects.get(pk=pk)
    dataemp['cdempresa'] = EmpresasForm(instance=dataemp['db'])
    return render(request, 'cd_empresa.html', dataemp)

def editprod(request, pk):
    dataprod = {}
    dataprod['db'] = Produtos.objects.get(pk=pk)
    dataprod['cdproduto'] = ProdutosForm(instance=dataprod['db'])
    return render(request, 'cd_produto.html', dataprod)

def updateseg(request, pk):
    data = {}
    data['db'] = Segmentos.objects.get(pk=pk)
    form = SegmentosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return HttpResponseRedirect ("/")

def updateemp(request, pk):
    dataemp = {}
    dataemp['db'] = Empresas.objects.get(pk=pk)
    cd_empresa = EmpresasForm(request.POST or None, instance=dataemp['db'])
    if cd_empresa.is_valid():
        cd_empresa.save()
        return HttpResponseRedirect ("/")

def updateprod(request, pk):
    dataprod = {}
    dataprod['db'] = Produtos.objects.get(pk=pk)
    cd_produto = ProdutosForm(request.POST or None, instance=dataprod['db'])
    if cd_produto.is_valid():
        cd_produto.save()
        return HttpResponseRedirect ("/")