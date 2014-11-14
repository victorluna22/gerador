# coding: utf-8
from django.db import models

# Create your models here.

class Advogado(models.Model):
	nome = models.CharField(u"Nome", max_length=255)
	oab = models.CharField(u"OAB", max_length=30)

	def __unicode__(self):
		return self.nome

class Imovel(models.Model):
	advogado = models.ForeignKey(Advogado)
	nome = models.CharField(u"Nome", max_length=255, null=True, blank=True)
	email = models.EmailField(u"E-mail", max_length=120, null=True, blank=True)
	telefone = models.CharField(u"Telefone", max_length=20, null=True, blank=True)
	logradouro = models.CharField(u"Logradouro", max_length=120, null=True, blank=True)
	numero = models.CharField(u"Numero", max_length=20, null=True, blank=True)
	complemento = models.CharField(u"complemento", max_length=60, null=True, blank=True)
	bairro = models.CharField(u"Bairro", max_length=60, null=True, blank=True)
	cidade = models.CharField(u"Cidade", max_length=60, null=True, blank=True)
	estado = models.CharField(u"Estado", max_length=60, null=True, blank=True)
	cep = models.CharField(u"CEP", max_length=9, null=True, blank=True)

	class Meta:
		verbose_name = u"Imóvel"
		verbose_name_plural = u"Imóveis"

	def __unicode__(self):
		return self.nome


