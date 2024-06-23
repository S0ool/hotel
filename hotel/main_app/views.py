from django.shortcuts import render, redirect

from main_app.forms import RoomsForm, BookingsForm
from main_app.models import Booking, HotelRoom


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    ctx = {
        'guest': request.user
    }

    return render(request, 'main_app/index.html', ctx)


def booking(request):
    if not request.user.is_authenticated:
        return redirect('login')

    ctx = {
        'guest': request.user,
        'bookings': Booking.objects.all(),
        'form': BookingsForm(),
    }

    return render(request, 'main_app/booking.html', ctx)


def rooms(request):
    if not request.user.is_authenticated:
        return redirect('login')

    ctx = {
        'guest': request.user,
        'rooms': HotelRoom.objects.all(),
        'form': RoomsForm(),
    }

    return render(request, 'main_app/rooms.html', ctx)


def add_room(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        pass
    return redirect('rooms_page')


def delete_room(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        HotelRoom.objects.get(id=room_id).delete()
    return redirect('rooms_page')


def edit_room_page(request, room_id):
    if not request.user.is_authenticated:
        return redirect('login')
    room = HotelRoom.objects.get(id=room_id)
    ctx = {
        'guest': request.user,
        'room': room,
        'form': RoomsForm(instance=room),
    }
    return render(request, 'main_app/edit_room.html', ctx)


def edit_room(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        form = RoomsForm(request.POST, request.FILES, instance=HotelRoom.objects.get(id=room_id))
        if form.is_valid():
            form.save()
    return redirect('rooms_page')


def add_booking_page(request, room_id):
    if not request.user.is_authenticated:
        return redirect('login')
    ctx = {
        'room_id': room_id,
    }
    return render(request, 'main_app/add_booking.html', ctx)


def add_booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        booking = Booking(
            guest=request.user,
            checkin=request.POST.get('checkin'),
            checkout=request.POST.get('checkout'),
            room=HotelRoom.objects.get(id=request.POST.get('room_id')),
        )
        booking.save()

    return redirect('booking_page')


def delete_booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        Booking.objects.get(id=booking_id).delete()
    return redirect('booking_page')


def edit_booking_page(request, booking_id):
    if not request.user.is_authenticated:
        return redirect('login')
    booking = Booking.objects.get(id=booking_id)

    if booking.guest != request.user:
        return redirect('booking_page')

    ctx = {
        'booking': booking,
        'rooms': HotelRoom.objects.all(),
    }
    return render(request, 'main_app/edit_booking.html', ctx)


def edit_booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking =Booking.objects.get(id=booking_id)
        if booking.guest == request.user:
            if request.POST.get('checkin') == '':
                booking.checkin = booking.checkin
            else:
                booking.checkin = request.POST.get('checkin')
            if request.POST.get('checkout') == '':
                booking.checkout = booking.checkout
            else:
                booking.checkout = request.POST.get('checkout')
            booking.room = HotelRoom.objects.get(id=request.POST.get('room_id'))
            booking.save()
    return redirect('booking_page')
