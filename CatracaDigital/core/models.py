from datetime import date
from itertools import groupby

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone as tz


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
    def months(self):
        return self.registers.datetimes('time', 'month', order='DESC')

    def registers_for_month(self, month, year):
        return self.registers.filter(time__month=month, time__year=year)

    def registers_for_day(self, d, m, y):
        return self.registers.filter(time__day=d, time__month=m, time__year=y).order_by('time')

    @property
    def today_registers(self):
        return self.registers_for_day(date.today().day, date.today().month, date.today().year)

    @property
    def current_month_registers(self):
        return self.registers_for_month(date.today().month, date.today().year)

    @property
    def grouped_month_registers(self):
        return self._group_registers(self.month_registers)

    def grouped_registers(self, year, month):
        registers = self.registers.filter(time__month=month, time__year=year)
        return self._group_registers(registers)

    def _group_registers(self, registers):
        registers = sorted(registers, key=lambda e: tz.localtime(e.time).date())
        registers = groupby(registers, key=lambda e: tz.localtime(e.time).date())
        return [{'date': r, 'entries': list(e)} for r, e in registers]

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
