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

def view(request, pk):
    dataSeg = {}
    dataSeg['db'] = Segmentos.objects.get(pk=pk) 
    return render(request, 'view.html', dataSeg)

def viewProd(request, pk):
    data = {'db': Produtos.objects.get(pk=pk) }
    return render(request, 'viewProdutos.html', data)

def viewEmpresas(request, pk):
    dataEmpresa = {'db': Empresas.objects.get(pk=pk) }
    return render(request, 'viewEmpresas.html', dataEmpresa)

def edit(request, pk):
    data = {}
    data['db'] = Segmentos.objects.get(pk=pk)
    data['form'] = SegmentosForm(instance=data['db'])
    return redirect(request, 'view.html', data)

def update(request, pk):
    data = {}
    data['db'] = Segmentos.objects.get(pk=pk)
    form = SegmentosForm(request.POST or None, instace=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def deletarEmpresa(request, pk):
    db = Empresas.objects.get(pk=pk)
    db.delete()
    return HttpResponseRedirect("/")


def deletarProduto(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return HttpResponseRedirect("/")

def deletarSeg(request, pk):
    db = Segmentos.objects.get(pk=pk)
    db.delete()
    return HttpResponseRedirect("/")