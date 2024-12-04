from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Client

# Create your views here.

# - Homepage
def home(request):
    return render(request, 'client_manager/index.html')

# - Dashboard
@login_required(login_url='accounts/login')
def dashboard(request):

    my_clients = Client.objects.filter(user=request.user)

    context = {'clients': my_clients}

    return render(request, 'client_manager/dashboard.html', context=context)