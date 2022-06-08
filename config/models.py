from django.db import models
from api.models.company.models import Company
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils.translation import gettext as _
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, name, cpf, sex, phone, cep,
                     address, number, neighborhood, city, uf, isActive, isAdmin,
                     isEmpresa, isProfissional, tipoPlano, companyId):
        now = timezone.now()
        company = Company.objects.get(pk=companyId)
        email = self.normalize_email(email)
        user = self.model(email=email,
                          password=password,
                          name=name,
                          cpf=cpf,
                          sex=sex,
                          phone=phone,
                          cep=cep,
                          address=address,
                          number=number,
                          neighborhood=neighborhood,
                          city=city,
                          uf=uf,
                          isActive=isActive,
                          isAdmin=isAdmin,
                          isEmpresa=isEmpresa,
                          isProfissional=isProfissional,
                          tipoPlano=tipoPlano,
                          createdAt=now,
                          updatedAt=now,
                          companyId=company)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, name, cpf, sex, phone, cep,
                    address, number, neighborhood, city, uf, isActive, isAdmin,
                    isEmpresa, isProfissional, tipoPlano, companyId):
        return self._create_user(email, password, name, cpf, sex, phone, cep,
                                 address, number, neighborhood, city, uf, isActive, isAdmin,
                                 isEmpresa, isProfissional, tipoPlano, companyId)

    def create_superuser(self, email, password, name, cpf, sex, phone, cep,
                         address, number, neighborhood, city, uf, isActive, isAdmin,
                         isEmpresa, isProfissional, tipoPlano, companyId):
        user = self._create_user(email, password, name, cpf, sex, phone, cep,
                                 address, number, neighborhood, city, uf, isActive, isAdmin,
                                 isEmpresa, isProfissional, tipoPlano, companyId)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
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
    isEmpresa = models.BooleanField()
    isProfissional = models.BooleanField()
    tipoPlano = models.IntegerField(max_length=1, verbose_name=_('Tipo de plano'))
    createdAt = models.DateTimeField(auto_now=True, verbose_name=_('Data de Criação'))
    updatedAt = models.DateTimeField(auto_now=True, verbose_name=_('Data de Modificação'))
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Empresa'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'name', 'cpf', 'sex', 'phone', 'cep',
                       'address', 'number', 'neighborhood', 'city', 'uf', 'isActive', 'isAdmin',
                       'isEmpresa', 'isProfissional', 'tipoPlano', 'companyId']

    objects = UserManager()
