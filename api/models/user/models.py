from django.db import models
from api.models.company.models import Company
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils.translation import gettext as _


class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name=_('Nome'))
    cpf = models.CharField(max_length=100, verbose_name=_('CPF'))
    sex = models.CharField(max_length=100, verbose_name=_('Sexo'))
    email = models.EmailField(verbose_name=_('Email'), max_length=255, unique=True)
    password = models.CharField(max_length=100, verbose_name=_('Senha'))
    phone = models.CharField(max_length=15, verbose_name=_('Telefone'))
    cep = models.CharField(max_length=9, verbose_name=_('CEP'))
    address = models.CharField(max_length=100, verbose_name=_('Endereço'))
    number = models.CharField(max_length=100, verbose_name=_('Número da propriedade'))
    neighborhood = models.CharField(max_length=100, verbose_name=_('Bairro'))
    city = models.CharField(max_length=100, verbose_name=_('Cidade'))
    uf = models.CharField(max_length=2, verbose_name=_('UF'))
    isActive = models.BooleanField(default=True)
    isAdmin = models.BooleanField(default=False)
    isEmpresa = models.BooleanFiel()
    isProfissional = models.BooleanField()
    tipoPlano = models.IntegerField(max_length=1, verbose_name=_('Tipo de plano'))
    createdAt = models.DateTimeField(auto_now=True, verbose_name=_('Data de Criação'))
    updatedAt = models.DateTimeField(auto_now=True, verbose_name=_('Data de Modificação'))
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Empresa'))


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            cpf=cpf,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
