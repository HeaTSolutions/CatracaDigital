from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, resolve_url as r


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


def logout(request):
    auth_logout(request)
    return redirect(r('landing:index'))


def today(request):
    return render(request, 'today.html')


def employees(request):
    return render(request, 'employees.html')


@login_required
def company(request):
    return render(request, 'company.html')