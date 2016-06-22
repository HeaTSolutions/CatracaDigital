from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404, resolve_url as r
from django.utils import timezone as tz
from .models import Employee, Register


#############################################################################
# Authentication
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None and user.is_active:
                auth_login(request, user)
                return redirect(r('core:today'))
        return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    auth_logout(request)
    return redirect(r('landing:index'))


#############################################################################
# Registers
@login_required
def today(request):
    return render(request, 'today.html')


@login_required
def register(request, register_pk):
    register = get_object_or_404(Register, pk=register_pk)
    return render(request, 'register.html', {'register': register})


@login_required
def create_register(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    register = Register.objects.create(employee=employee, registered_by_manager=True)
    messages.add_message(request, messages.INFO, 'Horário marcado com sucesso para {} no horário {}'.format(
        employee.full_name,
        tz.localtime(register.time).time().strftime('%H:%M')
    ))
    return redirect(r('core:employees'))


@login_required
def report(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    if request.method == 'GET':
        return render(request, 'components/months_for_report.html', {
            'months': employee.months,
            'employee': employee
        })
    elif request.method == 'POST':
        return _timetable_for_employee(request, employee, 'report.html')


#############################################################################
# Employees

@login_required
def timetable(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    return _timetable_for_employee(request, employee, 'components/timetable.html')


@login_required
def employees(request):
    # Getting list of employees
    employees = request.user.company.employees.all().order_by('first_name', 'last_name')
    return render(request, 'employees.html', {'employees': employees})


@login_required
def employee(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    return render(request, 'employee.html', {'employee': employee})


@login_required
def remove_employee(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    employee.delete()
    messages.add_message(request, messages.INFO, 'Funcionário {} removido com sucesso.'.format(
        employee.full_name
    ))
    return redirect(r('core:employees'))


#############################################################################
# Companies
@login_required
def company(request):
    return render(request, 'company.html')


#############################################################################
# Auxiliary methods
def _timetable_for_employee(request, employee, template):
    month, year = (int(x) for x in request.POST['month'].split('-'))
    return render(request, template, {
        'registers': employee.grouped_registers(year, month),
        'employee': employee
    })
