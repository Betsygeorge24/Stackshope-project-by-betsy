from django.shortcuts import render,redirect
from core.models import *
from core.decorators import admin_required

@admin_required
def admin_dashboard_view(request):
    return render(request,'admindashboard.html')

# Create your views here.
