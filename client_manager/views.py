from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddClientForm, UpdateClientForm

from django.contrib.auth.decorators import login_required

from .models import Client

# Create your views here.

# - Homepage
def home(request):
    return render(request, 'client_manager/index.html')

# - Dashboard
@login_required(login_url='accounts/login')
def dashboard(request):

    my_clients = Client.objects.filter(user=request.user)

    context = {'clients': my_clients}

    return render(request, 'client_manager/dashboard.html', context)


# - Add a client
@login_required(login_url='accounts/login')
def add_client(request):

    form = AddClientForm()

    if request.method == "POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)  
            client.user = request.user      
            client.save() 
            return redirect('dashboard')
    
    context = {'form': form}

    return render(request, 'client_manager/add-client.html', context)

# - Updaate a client
@login_required(login_url='accounts/login')
def update_client(request, pk):
    # Get the client or return a 404 error if not found
    client = get_object_or_404(Client, id=pk, user=request.user)

    # Initialize the form with the existing client data
    form = UpdateClientForm(instance=client)

    if request.method == "POST":
        form = UpdateClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'client': client} 
    return render(request, 'client_manager/update-client.html', context)

# - Read a singular client

@login_required(login_url='accounts/login')
def view_client(request, pk):
    
    all_clients = Client.objects.get(id=pk)

    context = {'client':all_records}

    return render(request, 'client_manager/view-client.html', context)

@login_required(login_url='accounts/login')
def singular_client(request, pk):
    try:
        # Ensure that the client belongs to the logged-in user
        client = Client.objects.get(id=pk, user=request.user)

        context = {'client': client}
        return render(request, 'client_manager/view-client.html', context)
    
    except Client.DoesNotExist:
        # If the client does not exist or doesn't belong to the logged-in user
        return redirect('dashboard')