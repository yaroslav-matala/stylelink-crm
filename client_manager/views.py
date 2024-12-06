from django.core.paginator import Paginator
from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddClientForm, UpdateClientForm

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden

from .models import Client

from django.contrib import messages

# Create your views here.

# - Homepage
def home(request):
    return render(request, 'client_manager/index.html')

# - Dashboard
@login_required(login_url='accounts/login')
def dashboard(request):

    search_query = request.GET.get('search', '')
    my_clients = Client.objects.filter(user=request.user)

    if search_query:
        my_clients = my_clients.filter(name__icontains=search_query)

    # Add pagination
    paginator = Paginator(my_clients, 5) 
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }

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

            messages.success(request, "New client was added")

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

            messages.success(request, "Client updated successfully")

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

# - Delete a record

@login_required(login_url='accounts/login')
def delete_client(request, pk):

    # Ensure the client exists and belongs to the logged-in user
    client = get_object_or_404(Client, id=pk, user=request.user)

    client.delete()

    messages.success(request, "Client deleted successfully")

    return redirect('dashboard')