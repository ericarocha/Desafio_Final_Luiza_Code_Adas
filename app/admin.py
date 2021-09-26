from django.contrib import admin
from django.db import models
from app.models import Segmentos, Empresas, Produtos

admin.site.register(Segmentos)
admin.site.register(Empresas)
admin.site.register(Produtos)
