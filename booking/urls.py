from django.urls import path 
from .views import *
urlpatterns=[
    path('bkf/<int:flight_id>',book_flight,name='book'),
    path('mybook/',my_bookings,name='mybookings'),
    path('cancel/<int:id>',cancel,name='cancel')
]