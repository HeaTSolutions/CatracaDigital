from django.contrib import admin

from .models import Employee, Register, Company


class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = 'mobile_id', 'first_name', 'last_name', 'pis', 'admission_date', 'created_at', 'modified_at'
    search_fields = 'first_name', 'last_name'


class RegisterModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'mobile_id', 'employee_name', 'time', 'latitude', 'longitude'

    def employee_name(self, obj):
        return obj.employee.full_name

    def mobile_id(self, obj):
        return obj.employee.mobile_id

    mobile_id.short_description = 'código do celular'
    employee_name.short_description = 'nome do funcionário'


class CompanyModelAdmin(admin.ModelAdmin):
    list_display = 'name', 'cnpj', 'city', 'state', 'manager'
    search_fields = 'name', 'manager','state',


admin.site.register(Employee, EmployeeModelAdmin)
admin.site.register(Register, RegisterModelAdmin)
admin.site.register(Company, CompanyModelAdmin)
