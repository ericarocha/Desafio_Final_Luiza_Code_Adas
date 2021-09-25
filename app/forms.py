from django.db import models
from django.forms import ModelForm
from app.models import Segmentos, Voltagens,  Empresas, Produtos

class SegmentosForm(ModelForm):
    class Meta:
        model = Segmentos
        fields = "__all__"

class VoltagensForm(ModelForm):
    class Meta:
        model = Voltagens
        fields = "__all__"

class EmpresasForm(ModelForm):
    class Meta:
        model = Empresas
        fields = "__all__"

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = "__all__"





