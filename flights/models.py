from django.db import models

# Create your models here.
class Fight(models.Model):
    flight_number=models.CharField(max_length=10)
    airline=models.CharField(max_length=20)

    source=models.CharField(max_length=40)
    destination=models.CharField(max_length=40)

    departure=models.DateTimeField()
    arrival=models.DateTimeField()

    price=models.DecimalField(max_digits=8,decimal_places=2)
    seats=models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.flight_number