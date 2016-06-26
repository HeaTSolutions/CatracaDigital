from django.utils import timezone
from rest_framework import test, status
from ...core.models import Employee
from django.shortcuts import resolve_url as r


class EmployeeAPIEndpointTest(test.APITestCase):
    def setUp(self):
        self.mobile_id = 'abc123'
        Employee(
            first_name='Henrique',
            last_name='Nogueira',
            mobile_id=self.mobile_id,
            admission_date=timezone.now(),
            pis='meu pis'
        ).save()
        self.resp = self.client.get(r('api:employee-detail', self.mobile_id))

    def test_view_get_status(self):
        '''GET /employee/mobile_id should return 200'''
        self.assertEqual(status.HTTP_200_OK, self.resp.status_code)

    def test_view_get_content(self):
        '''GET /employee/mobile_id should return employee info'''
        expected = 'first_name', 'last_name', 'pk', 'modified_at'
        for e in expected:
            with self.subTest():
                self.assertTrue(e in self.resp.data)

        with self.subTest():
            self.assertEqual(self.mobile_id, self.resp.data['pk'])