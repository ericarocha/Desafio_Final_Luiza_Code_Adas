from django.db import models

class Segmentos (models.Model):
    nome = models.CharField(max_length=150)
    def __str__(self):
        return str(self.nome)

class Voltagens (models.Model):
    tipo = models.CharField(max_length=10)
    def __str__(self):
        return str(self.tipo)

class Empresas (models.Model):
    id_segmento = models.ForeignKey(Segmentos, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    cnpj = models.IntegerField()
    def __str__(self):
        return str(self.nome)

class Produtos (models.Model):
    id_empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE) 
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    id_voltagem = models.ForeignKey(Voltagens, on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=15)
    preço = models.CharField(max_length=15) 
    quantidade = models.IntegerField()
    # imagem = models.ImageField(upload_to = 'imagens', blank=True, null=True)






