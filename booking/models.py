from django.db import models
from django.contrib.auth.models import User
from flights.models import Fight
# Create your models here.
class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    flight=models.ForeignKey(Fight,on_delete=models.CASCADE)
    passenger_name=models.CharField(max_length=30)
    seat_number=models.CharField(max_length=10)
    booking_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username+'-'+self.flight.flight_number
