from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase
from ..models import Employee


class EmployeeTest(TestCase):
    def setUp(self):
        self.employee_data = {
            'first_name': 'Henrique',
            'last_name': 'Nogueira',
            'pis': '01234',
            'admission_date': datetime.today(),
            'mobile_id': '#123'
        }

        self.e = Employee(**self.employee_data)
        self.e.save()

    def test_created(self):
        '''Employee entity should be created on database'''
        self.assertTrue(Employee.objects.exists())

    def test_first_name_type(self):
        '''Employee first name should be a string'''
        self.assertIsInstance(self.e.first_name, str)

    def test_first_name(self):
        '''Employee name should not be modified'''
        self.assertEquals('Henrique', self.e.first_name)

    def test_last_name_type(self):
        '''Employee last name should be a string'''
        self.assertIsInstance(self.e.last_name, str)

    def test_last_name_value(self):
        '''Employee last name should not be modified'''
        self.assertEquals('Nogueira', self.e.last_name)

    def test_created_at(self):
        '''Employee should have a created_at attribute'''
        self.assertIsInstance(self.e.created_at, datetime)

    def test_modified_at(self):
        '''Employee should have a modified_at attribute'''
        self.assertIsInstance(self.e.modified_at, datetime)

    def test_full_name(self):
        '''Full name should be formatted'''
        self.assertEquals('Henrique Nogueira', self.e.full_name)

    def test_model_str(self):
        '''Print format should be correct'''
        self.assertEqual('[#123] Henrique Nogueira', str(self.e))

    def test_mobile_id_duplicate(self):
        '''Employee mobile_id should be unique'''
        e_dup = Employee(**self.employee_data)

        with self.assertRaises(IntegrityError):
            e_dup.save()
