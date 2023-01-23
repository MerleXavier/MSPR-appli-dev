#import scan
from django.shortcuts import render
from django.db import models

def dashboard(request):
    metrics = scan.objects.all()
    return render(request, 'dashboard.html', {'metrics': metrics})