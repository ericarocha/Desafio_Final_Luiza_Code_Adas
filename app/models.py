from django.db import models

class Segmentos(models.Model):
segmento = models.ForeignKeye(Eletrodomesticos, Cosmeticos, Informatica, Supermecado, Vestuario, on_delete=models.CASCADE)

class Eletrodomesticos(models.Model):
    eletro_marca = models.CharField(max_length=150)
    eletro_produto = models.CharField(max_length=150)
    eletro_descricao = models.TextField(blank=True, null=true)
    eletro_voltagem = models.CharField(max_length=15)
    eletro_preço = models.CharField(max_length=15) 
    quantidade = models.IntegerField()
    
class Cosmeticos(models.Model):
    cosm_marca = models.CharField(max_length=150)
    cosm_produto = models.CharField(max_length=150)
    cosm_descricao = models.TextField(blank=True, null=true)
    cosm_preço = models.CharField(max_length=15)
    

class Informatica(models.Model):
    inf_marca = models.CharField(max_length=150)
    inf_produto = models.CharField(max_length=150)
    inf_descricao = models.TextField(blank=True, null=true)
    inf_preço = models.CharField(max_length=15)

class Supermecado(models.Model):
    marca = models.CharField(max_length=150)
    produto = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    preço = models.CharField(max_length=15)

class Vestuario(models.Model):
    marca = models.CharField(max_length=150)
    produto = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=true)
    preço = models.CharField(max_length=15)

