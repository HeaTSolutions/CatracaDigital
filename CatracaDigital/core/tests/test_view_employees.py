from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from ..models import Company, Employee


class EmployeesViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('user', 'email@domain.com', 'password')
        company = Company.objects.create(**{
            'name': 'My company',
            'cnpj': '0123456789',
            'address': '123 John street',
            'city': 'New York',
            'state': 'NY',
            'manager': user
        })

        Employee.objects.create(**{
            'first_name': 'Henrique',
            'last_name': 'Nogueira',
            'pis': '01234',
            'admission_date': datetime.today(),
            'mobile_id': '#123',
            'company': company
        })

        self.client.login(username='user', password='password')
        self.r = self.client.get(r('core:employees'))

    def test_context(self):
        '''Employees view should contain employees context'''
        self.assertIn('employees', self.r.context)

    def test_template_used(self):
        '''Employees should render employees.html'''
        self.assertTemplateUsed(self.r, 'employees.html')