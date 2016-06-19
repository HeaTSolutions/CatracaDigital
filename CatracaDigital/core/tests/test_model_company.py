from django.contrib.auth.models import User
from django.test import TestCase
from ..models import Company


class CompanyModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='test_password')
        self.c_data = {
            'name': 'My company',
            'cnpj': '0123456789',
            'address': '123 John street',
            'city': 'New York',
            'state': 'NY',
            'manager': user
        }
        self.company = Company.objects.create(**self.c_data)

    def test_entity_exists(self):
        '''Company should be created on DB'''
        self.assertTrue(Company.objects.exists())

    def test_name(self):
        '''Company should have a string name'''
        self.assertIsInstance(self.company.name, str)

    def test_cnpj(self):
        '''Company should have a string cnpj'''
        self.assertIsInstance(self.company.cnpj, str)

    def test_address(self):
        '''Company should have a string address'''
        self.assertIsInstance(self.company.address, str)

    def test_city(self):
        '''Company should have a string city'''
        self.assertIsInstance(self.company.city, str)

    def test_state(self):
        '''Company should have a string state with two letters'''
        with self.subTest():
            self.assertIsInstance(self.company.state, str)
            self.assertEqual(2, len(self.company.state))