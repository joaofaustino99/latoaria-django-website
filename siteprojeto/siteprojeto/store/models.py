import os

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime

class Tamanho(models.Model):
    nome_tamanho = models.CharField(max_length=200)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Compra(models.Model):
    customer = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField('data compra', default=datetime.datetime.now)
    preco_total = models.FloatField(default=0.0)
    complete = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(str(self.customer) + " ---Compra_ID = " + str(self.id))

    @property
    def obter_total_compra(self):
        items = self.itemscompra_set.all()
        total = sum([item.obter_total for item in items])
        return total

    @property
    def obter_total_items(self):
        items = self.itemscompra_set.all()
        total = sum([item.quantidade for item in items])
        return total



class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200, default='')
    descricao_grande = models.CharField(max_length=200, default='')
    tamanho = models.ManyToManyField(Tamanho, null=True, blank=True)
    imagem = models.ImageField(null=True, blank=True)
    preco = models.FloatField()

    def __str__(self):
        return self.nome

    @property
    def imageURL(self):
        try:
            url = self.imagem.url
        except:
            url = ''
        return url



class productImage(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="store/static/store/images/")


    def __str__(self):
        return self.produto.nome


class ItemsCompra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField(default=1, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    @property
    def obter_total(self):
        total = self.produto.preco * self.quantidade
        return total

    def __str__(self):
        return str(self.produto) + " -> x" + str(self.quantidade) 


class Morada_envio(models.Model):
    customer = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, null=True)
    morada = models.CharField(max_length=200, null=False)
    cidade = models.CharField(max_length=200, null=False)
    concelho = models.CharField(max_length=200, null=False)
    codigo_postal = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.morada + "->" + str(self.customer)
