from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from flights.models import Fight

# Create your views here.
@login_required(login_url='login')
def book_flight(req,flight_id):
    flight=get_object_or_404(Fight,id=flight_id)
    if req.method=='POST':
        a=req.POST['pname']
        b=req.POST['snum']
        Booking.objects.create(
            user=req.user,
            flight=flight,
            passenger_name=a,
            seat_number=b,
        )
        return redirect('mybookings')
    return render(req,'booking.html',{'data':flight})
def my_bookings(req):
    bookings=Booking.objects.filter(user=req.user)
    print(bookings)
    return render(req,'mybook.html',{'data':bookings})
@login_required(login_url='login')
def cancel(req,id):
    b_f=get_object_or_404(Booking,id=id)
    if req.method=='POST':
        b_f.delete()
        return redirect(my_bookings)
    return redirect(my_bookings)