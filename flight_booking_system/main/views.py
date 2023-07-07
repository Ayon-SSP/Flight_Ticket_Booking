from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .models import Flight


@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})



def add_flight(request):
    if request.method == 'POST':
        flight_name = request.POST['flight_name']
        departure_time = request.POST['departure_time']
        flight = Flight(flight_name=flight_name, departure_time=departure_time)
        flight.save()
        return redirect('home')
    return render(request, 'main/add_flight.html')