from datetime import date
from itertools import groupby

from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    '''
    Model that represents an employee on a company
    '''
    mobile_id = models.CharField('código celular', max_length=255, primary_key=True)
    company = models.ForeignKey('Company', related_name='employees', help_text='empresa', null=True)
    first_name = models.CharField('nome', max_length=255)
    last_name = models.CharField('sobrenome', max_length=255)
    pis = models.CharField('PIS', max_length=255)
    admission_date = models.DateField('data de admissão')
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        verbose_name = 'empregado'
        verbose_name_plural = 'empregados'

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def today_registers(self):
        return self.registers.filter(time__date=date.today())

    @property
    def month_registers(self):
        return self.registers.filter(time__month=date.today().month, time__year=date.today().year)

    @property
    def grouped_month_registers(self):
        registers = sorted(self.month_registers, key=lambda e: e.time)
        registers = groupby(registers, key=lambda e: e.time.date())

        result = []
        for r, e in registers:
            result.append({'date': r, 'entries': list(e)})

        return result

    def __str__(self):
        return '[{}] {} {}'.format(self.mobile_id, self.first_name, self.last_name)


class Register(models.Model):
    '''
    Represents a register of an employee on a company
    '''
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='registers')
    time = models.DateTimeField('marcação', auto_now_add=True)
    latitude = models.FloatField('latitude', default=0)
    longitude = models.FloatField('longitude', default=0)
    registered_by_manager = models.BooleanField(default=False)

    class Meta:
        ordering = 'time',
        verbose_name = 'registro de ponto'
        verbose_name_plural = 'registros de ponto'

    def __str__(self):
        return '{} - {}'.format(self.time, self.employee.full_name)


class Company(models.Model):
    name = models.CharField('nome da empresa', max_length=255)
    cnpj = models.CharField('CNPJ', max_length=255)
    address = models.CharField('endereço', max_length=255)
    city = models.CharField('cidade', max_length=255)
    state = models.CharField('estado', max_length=2)
    manager = models.OneToOneField(User, related_name='company', help_text='Gestor da loja')

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'

    def __str__(self):
        return self.name
