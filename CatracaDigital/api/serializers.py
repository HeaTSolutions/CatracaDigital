from django.shortcuts import get_object_or_404
from ..core.models import Employee, Register, Company
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    '''Tells Django how to serialize a Company'''
    class Meta:
        model = Company
        fields = 'name',


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    '''Tells Django how to serialize the Employee instances'''

    company = CompanySerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = 'pk', 'first_name', 'last_name', 'full_name', 'company', 'pis', 'admission_date', 'created_at', 'modified_at'
        read_only_fields = 'first_name', 'last_name', 'full_name', 'created_at', 'modified_at'


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    '''Tells Django how to serialize a Register instance'''

    employee = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = Register
        fields = 'pk', 'time', 'latitude', 'longitude', 'employee'
        read_only_fields = 'employee',

    def create(self, validated_data):
        employee_pk = self.initial_data['employee']
        employee = get_object_or_404(Employee, pk=employee_pk)
        return Register.objects.create(employee=employee)
