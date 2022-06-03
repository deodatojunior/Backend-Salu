from django.db import models
from django.utils.translation import gettext as _


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Nome'))
    email = models.EmailField(verbose_name=_('Email'), max_length=255, unique=True)
    cep = models.CharField(max_length=9, verbose_name=_('CEP'))
    address = models.CharField(max_length=100, verbose_name=_('Endereço'))
    numberAddress = models.CharField(max_length=100, verbose_name=_('Nº'))
    neighborhood = models.CharField(max_length=100, verbose_name=_('Bairro'))
    city = models.CharField(max_length=100, verbose_name=_('Cidade'))
    uf = models.CharField(max_length=2, verbose_name=_('UF'))