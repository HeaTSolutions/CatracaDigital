from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from ..models import Company


class CompanyViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('user', 'email@domain.com', 'password')
        Company.objects.create(
            **{
                'name': 'My company',
                'cnpj': '0123456789',
                'address': '123 John street',
                'city': 'New York',
                'state': 'NY',
                'manager': user
            }
        )
        self.client.login(username='user', password='password')
        self.r = self.client.get(r('core:company'))

    def test_status_code(self):
        '''Company page should return 200'''
        self.assertEqual(200, self.r.status_code)

    def test_company_data(self):
        '''View should contain company information'''
        expected = (
            'My company',
            '0123456789',
            '123 John street',
            'New York',
            'NY'
        )
        with self.subTest():
            for exp in expected:
                self.assertContains(self.r, exp)

    def test_renders_menu(self):
        '''Company view should render menu'''
        expected = [
            'Hoje',
            'Funcionários',
            'Minha empresa',
            'Sair'
        ]
        with self.subTest():
            for exp in expected:
                self.assertContains(self.r, exp)