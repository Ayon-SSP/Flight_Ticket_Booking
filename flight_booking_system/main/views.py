import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .models import Flight
from django.db.models import Q

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


@login_required(login_url='/login')
def flight_list(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        flights = Flight.objects.filter(
            Q(departure_time__gte=start_date) &
            Q(departure_time__lte=end_date)
        ).order_by('departure_time')
        # print(flights)
    else:
        flights = Flight.objects.order_by('departure_time')

    return render(request, 'main/flight_list.html', {'flights': flights})

@login_required(login_url='/login')
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    seats = flight.seats

    available_seats = {i+1: seats[i] is -1 for i in range(len(seats)) if seats[i] is -1}
    print(available_seats)
    if request.method == 'POST':
        seat_number = int(request.POST['seat_number'])
        user_id = request.POST['user_id']
        print(seat_number,user_id)

        if seat_number in available_seats and available_seats[seat_number]:
            seats[seat_number-1] = user_id
            flight.save()
            flights = Flight.objects.order_by('departure_time')
            # redirect('flight_list', flights= flights)
            return render(request, 'main/flight_list.html', {'flights': flights})

    return render(request, 'main/book_flight.html', {'flight': flight, 'available_seats': available_seats})


@login_required(login_url='/login')
def user_bookings(request, user_id):
    bookings = Flight.objects.filter(seats__contains=[user_id])
    return render(request, 'main/user_bookings.html', {'bookings': bookings})

@login_required(login_url='/login')
def add_flight(request):
    if request.method == 'POST':
        flight_name = request.POST['flight_name']
        departure_time = request.POST['departure_time']
        flight = Flight(flight_name=flight_name, departure_time=departure_time)
        flight.save()
        return redirect('home')
    return render(request, 'main/add_flight.html')

@login_required(login_url='/login')
def remove_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    flight.delete()
    return redirect('flight_list')