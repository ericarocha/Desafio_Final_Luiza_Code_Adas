from django.db import models
from django.forms import ModelForm
from app.models import Segmentos, Marcas, Produtos

class SegmentosForm(ModelForm):
    class Meta:
        model = Segmentos
        fields = "__all__"

class MarcasForm(ModelForm):
    class Meta:
        model = Marcas
        fields = "__all__"

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = "__all__"





