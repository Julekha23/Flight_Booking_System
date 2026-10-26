from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(req):
    if req.method=='POST':
        a=req.POST['fname']
        b=req.POST['lname']
        c=req.POST['email']
        d=req.POST['uname']
        e=req.POST['password']
        try:
            u=User.objects.get(username=d)
            return render(req,'register.html',{'error':'Username is Already exist'})
        except User.DoesNotExist:
            u=User.objects.create(
            first_name=a,
            last_name=b,
            email=c,
            username=d,
            )
            u.set_password(e)
            u.save()
            return redirect('home')
    return render(req,'register.html')
def login_(req):
    if req.method=='POST':
        a=req.POST['uname']
        b=req.POST['password']
        user=authenticate(req,username=a,password=b)
        if user is not None:
            login(req,user)
            return redirect('home')
        else:
            return render(req,'login.html',{'error':"Invalid credentials"})
    return render(req,'login.html')
@login_required(login_url='login')
def logout_(req):
    logout(req)
    return redirect('home')
@login_required(login_url='login')
def profile(req):
    return render(req,'profile.html')