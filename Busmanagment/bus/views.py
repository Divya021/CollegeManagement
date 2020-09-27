from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def nav(request):
    return render(request,'carousel.html')


def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')


def Login_customer(request):
    if request.method == "POST":
        n = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=n,password=p)
        if user.username=="admin":
            login(request, user)
            return redirect("admindashboard")
        elif user:
            login(request, user)
            return redirect('dashboard')
    return render(request,'login_customer.html')

def Register_customer(request):
    if request.method == "POST":
        n = request.POST['uname']
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        a = request.POST['add']
        m = request.POST['mobile']
        g = request.POST['male']
        d = request.POST['birth']
        p = request.POST['pwd']
        user = User.objects.create_user(first_name=f,last_name=l,username=n,password=p,email=e)
        Register.objects.create(user=user,add=a,mobile=m,gender=g,dob=d)
    return render(request,'register_customer.html')

def Search_Bus(request):
    error=False
    data=Add_Bus.objects.all()
    data2=Add_route.objects.all()
    data3=0
    fare3 = 0
    if request.method=="POST":
        f = request.POST["fcity"]
        t = request.POST["tcity"]
        da = request.POST["date"]
        bus = 0
        bus1 = 0
        bus2 = 0
        fare2 = 0
        fare1 = 0
        fare3 = 0
        for i in data2:
            if i.route==f:
                bus = i.bus.busname
                fare2=i.fare

        for j in data2:
            if j.route==t:
                bus1 = j.bus.busname
                fare1=j.fare

        fare3=fare2-fare1
        if bus == bus1:
            bus2=bus
            error=True

        data3 = Add_Bus.objects.filter(busname=bus2).get()
    d={"data":data,"data2":data2,'data3':data3,'fare3':fare3,"error":error}
    return render(request,'search_bus.html',d)


def Dashboard(request):
    return render(request,'dashboard.html')

def admindashboard(request):
    return render(request,'admindashboard.html')

def Logout(request):
    logout(request)
    return redirect('nav')
def Add_bus(request):
    error=False
    if request.method == "POST":
        n = request.POST['busname']
        no = request.POST['bus_no']
        f = request.POST['fcity']
        to= request.POST['tcity']
        de= request.POST['dtime']
        a = request.POST['atime']
        t = request.POST['ttime']
        d = request.POST['dis']
        i = request.POST['img']
        Add_Bus.objects.create(busname=n,bus_no=no,from_city=f,to_city=to,departuretime=de,arrivaltime=a,trevaltime=t,distance=d,img=i)
        error=True
        return redirect("view_bus")
    d={"error":error}


    return render(request,'add_bus.html',d)
def view_bus(request):
    data=Add_Bus.objects.all()
    d={"data":data}
    return render(request,"view_bus.html",d)
def add_route(request):
    error=False
    data=Add_Bus.objects.all()

    if request.method == "POST":
        b = request.POST['bus']
        r = request.POST['route']
        f= request.POST['fare']
        d = request.POST['dis']
        bus1 = Add_Bus.objects.filter(id=b).get()
        Add_route.objects.create(bus=bus1,route=r,distance=d,fare=f)
        error=True
    d={"data":data,"error":error}

    return render(request,'add_route.html',d)
def edit(request,pid):
    #if not request.user.is_authenticated:
        #return redirect('login')

    data1=Add_Bus.objects.get(id=pid)
    if request.method == "POST":
        n = request.POST['busname']
        no = request.POST['bus_no']
        de= request.POST['dtime']
        a = request.POST['atime']
        t = request.POST['ttime']
        f = request.POST['fcity']
        to= request.POST['tcity']
        d = request.POST['dis']
        data1.busname=n
        data1.bus_no=no
        data1.from_city=f
        data1.to_city=to
        data1.departuretime=de
        data1.arrivaltime=a
        data1.traveltime=t
        data1.distance=d
        data1.save()
        return redirect("view_bus")
    d = {'data':data1}
    return render(request,'editbus.html',d)

def delete(request,pid):
    error=False
    data=Add_Bus.objects.get(id=pid)
    data.delete()
    return redirect("view_bus")
    return render(request,"view_bus.html")

def displayroute(request):
    li=[]
    data=Add_route.objects.all()
    if data.bus==307:
        a=data.route
    d={"a":a}
    return render(request,"availableroute.html",d)


