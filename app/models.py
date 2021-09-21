from django.db import models
from django.db.models.constraints import UniqueConstraint

class Segmentos (models.Model):
    segmento = models.CharField(max_length=150)
    descricao_segmento = models.CharField(max_length=255)


class Marcas (models.Model):
    segmento_marca = models.ForeignKey(Segmentos, on_delete=models.CASCADE)
    nome_empresa_marca = models.CharField(max_length=150)
    cnpj = models.FloatField(UniqueConstraint)



class Produtos (models.Model):
    produto_marca_key = models.ForeignKey(Marcas, on_delete=models.CASCADE) 
    segmento_produto_models = models.CharField(max_length=150)
    produto = models.CharField(max_length=150)
    produto_nome = models.CharField(max_length=150)
    produto_descricao = models.TextField(blank=True, null=True)
    produto_voltagem = models.CharField(max_length=15)
    produto_tamanho = models.CharField(max_length=15)
    produto_preço = models.CharField(max_length=15) 
    produto_quantidade = models.IntegerField()
    produto_foto = models.FileField()

