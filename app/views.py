from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def home(request):
    table = Table.objects.all()
    booking_list = Booking_drink.objects.filter(status=True,cancel=False)
    print(booking_list)
    return render(request,'home.html',{'table':table,'booking_list':booking_list})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

    return render(request,'login.html')

def sign_out(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request,'profile.html' ,)

def editprofile(request):
    form = EditForm(instance=request.user)
    if request.method == 'POST':
        form = EditForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = EditForm()
    else:
        form = EditForm(instance=request.user)

    return render(request,'editprofile.html',{'form':form})

def booking(request,id):
    table = Table.objects.get(pk=id)
    bookings = Booking_drink.objects.create(
        user=request.user,
        table=table,
    )
    bookings.save()
    table.user = request.user
    table.save()
    return redirect('booking_list')

@login_required
def booking_list(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            booking_list = Booking_drink.objects.filter(cancel=False).order_by('-date')
        else:
            booking_list = Booking_drink.objects.filter(user=request.user,cancel=False)
    return render(request,'booking_list.html',{'booking_list':booking_list})

def permissions(request,id):
    booking_list = Booking_drink.objects.get(pk=id)
    booking_list.status = True
    booking_list.cancel = False
    booking_list.save()

    table = Table.objects.get(id=booking_list.table_id)
    table.status = True
    table.user = booking_list.user
    table.save()
    return redirect('booking_list')

def permissions_no(request,id):
    booking_list = Booking_drink.objects.get(pk=id)
    booking_list.cancel = True
    booking_list.status = False
    booking_list.save()

    table = Table.objects.get(id=booking_list.table_id)
    table.status = False
    table.save()

    return redirect('booking_list')

def reset(request):
    tables = Table.objects.all()
    booking_list = Booking_drink.objects.all()
    for booking in booking_list:
        booking.status = False
        booking.cancel = True
        booking.save()
    # booking_list.cancel = True
    for table in tables:
        table.status = False
        table.save()
    return redirect('/')

def cancel_booking(request,id):
    booking_list = Booking_drink.objects.get(pk=id,user=request.user)
    booking_list.cancel = True
    booking_list.save()
    return redirect('booking_list')

    
