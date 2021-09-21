from django.forms import ModelForm, fields
from app.models import Segmentos, Marcas, Produtos

class SegmentosForm(ModelForm):
    class Meta:
        model : Segmentos
        fields = ['segmento', 'descricao_segmento']

class MarcasForm(ModelForm):
    class Meta:
        model : Marcas
        fields = ['segmento_marca', 'nome_empresa_marca', "cpnj"]

class ProdutosForm(ModelForm):
    class Meta:
        model : Produtos
        fields = ["Produto_marca_key", "segmento_produto_models", "produto", "produto_nome", "produto_descricao","produto_voltagem", "produto_tamanho", "produto_preço", "produto_quantidade", "produto_foto"]





