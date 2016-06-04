from django.shortcuts import render
from .models import Plan


def index(request):
    return render(request, 'landing/index.html', {'plans': Plan.objects.all()})
