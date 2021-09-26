"""adas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, form, cd_produto, cd_empresa, create, create2, createprod, viewseg, viewProd , viewEmpresas,editseg, editemp, editprod, updateseg, updateemp, updateprod, deletarEmpresa, deletarProduto, deletarSeg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('cd_produto/', cd_produto, name='cd_produto'),
    path('cd_empresa/', cd_empresa, name='cd_empresa'),
    path('create/', create, name='create'),
    path('create2/', create2, name='create2'),
    path('createprod/', createprod, name='createprod'),
    path('viewseg/<int:pk>/', viewseg, name='viewseg'),
    path('viewProd/<int:pk>/', viewProd, name='viewProd'),
    path('viewEmpresas/<int:pk>/', viewEmpresas, name='viewEmpresas'),
    path('editseg/<int:pk>/', editseg, name='editseg'),
    path('editemp/<int:pk>/', editemp, name='editemp'),
    path('editprod/<int:pk>/', editprod, name='editprod'),
    path('updateseg/<int:pk>/', updateseg, name='updateseg'),
    path('updateemp/<int:pk>/', updateemp, name='updateemp'),
    path('updateprod/<int:pk>/', updateprod, name='updateprod'),
    path('deletarEmpresa/<int:pk>/', deletarEmpresa, name='deletarEmpresa'),
    path('deletarProduto/<int:pk>/', deletarProduto, name='deletarProduto'),
    path('deletarSeg/<int:pk>/', deletarSeg, name='deletarSeg')
]