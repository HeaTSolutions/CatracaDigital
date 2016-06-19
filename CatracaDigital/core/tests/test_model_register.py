from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase
from ..models import Employee, Register


class RegisterTest(TestCase):
    def setUp(self):
        employee_data = {
            'first_name': 'Henrique',
            'last_name': 'Nogueira',
            'pis': '01234',
            'admission_date': datetime.today(),
            'mobile_id': '#123'
        }
        e = Employee.objects.create(**employee_data)
        self.register = Register.objects.create(employee=e, latitude=1.0, longitude=1.0)

    def test_create(self):
        '''Register should be created on datbase'''
        self.assertTrue(Register.objects.exists())

    def test_time(self):
        '''Register should contain time'''
        self.assertIsInstance(self.register.time, datetime)

    def test_latitude(self):
        '''Register should contain latitude'''
        self.assertIsInstance(self.register.latitude, float)

    def test_longitude(self):
        '''Register should contain longitude'''
        self.assertIsInstance(self.register.longitude, float)

    def test_employee(self):
        '''Register should be associated to an employee'''
        self.assertIsInstance(self.register.employee, Employee)

    def test_str(self):
        '''Register should be printed corectly'''
        self.assertTrue(str(self.register).endswith('- Henrique Nogueira'))


class RegisterFailTest(TestCase):
    def test_no_employee(self):
        '''Register should not be created without employee'''
        with self.assertRaises(IntegrityError):
            Register.objects.create(time=datetime.now())
