from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# - Homepage
def home(request):
    return render(request, 'client_manager/index.html')

# - Dashboard
@login_required(login_url='accounts/login')
def dashboard(request):
    return render(request, 'client_manager/dashboard.html')