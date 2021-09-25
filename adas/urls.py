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
from app.views import home, form, cd_produto, cd_empresa, create, create2, createprod, view, edit, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('cd_produto/', cd_produto, name='cd_produto'),
    path('cd_empresa/', cd_empresa, name='cd_empresa'),
    path('create/', create, name='create'),
    path('create2/', create2, name='create2'),
    path('createprod/', createprod, name='createprod'),
    path('view/<int:pk>', view, name='view'),
    path('edit/<int:pk>', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
]