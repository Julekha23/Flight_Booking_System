from django.shortcuts import render
from .models import *
# Create your views here.
def home(req):
    flight=[]
    if req.method=='GET' and req.GET.get('source'):
        source=req.GET.get('source')
        destination=req.GET.get('destination')
        date=req.GET.get('departure')
        print(date)
        flight=Fight.objects.filter(
            source__iexact=source,
            destination__iexact=destination,
            departure__date=date,
        )
        print(flight)
    return render(req,'home.html',{'fights':flight})