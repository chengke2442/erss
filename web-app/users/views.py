from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm,CarForm,RideForm
from .models import haha,Ride
from .models import car
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def register(request):
        
    if request.method=='POST':
        form = UserForm(request.POST)
        form2 = CarForm(request.POST)
        if (form.is_valid()) and (form2.is_valid()):
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                message = "check your password!"
                return render(request,'users/registeer.html',{'form':form,'car':form2})
            else:
                same = haha.objects.filter(email = email)
                if same:
                    message = "Email has has been registered!"
                    return render(request,'users/register.html',{'form':form,'car':form2})

                new_user = haha.objects.create()
                new_user.first_name = form.cleaned_data.get('first_name')
                new_user.last_name = form.cleaned_data.get('last_name')
                new_user.email= form.cleaned_data.get('email')
                new_user.password = password1
                new_user.status_flag = form.cleaned_data.get('status_flag')
                new_user.vehicle_id =  form.cleaned_data.get('plate_number')
                new_user.phone_number = form.cleaned_data.get('phone_number')
                new_user.save()
                new_car = car.objects.create()
                new_car.driver_id = new_user
                new_car.vehicle_type =  form2.cleaned_data.get('vehicle_type')
                new_car.plate_number =  form2.cleaned_data.get('plate_number')
                                                              
                new_car.max_passanger =  form2.cleaned_data.get('max_passanger')
                new_car.save()
            return redirect('/blog/')
    else:
        form = UserForm()
        form2 = CarForm()
    return render(request,'users/register.html',{'form':form,'car':form2})

def login(request):
    if request.session.get('is_login',None):
        return redirect('/login')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        message = "Please enter correct information"
        if email and password:
#           email = email.strip();
            try:
                 user = haha.objects.get(email=email)
                 if user.password == password:
                     request.session['is_login']=True
                     request.session['user_email']=user.email
                     request.session['user_id']=user.id
                     return redirect('/request/')
                 else:
                     message = "Incorrect password"
            except:
                message = "User dose not exist"
        return render(request, 'users/login.html', {"message": message})
    return render(request,'users/login.html')


def request(request):
    
    # display pages to request a ride
    if request.method =="POST":
        request_form = RideForm(request.POST)
        if request_form.is_valid():
            destination = request_form.cleaned_data.get('destination')
            arrivalTime = request_form.cleaned_data.get('arrivalTime')
            num = request_form.cleaned_data.get('NumPassanger')
            share = request_form.cleaned_data.get('CanShare')
#            new_request = Ride.objects.create(destination, arrivalTime, num, share)
            new_request = Ride.objects.create();
           
            new_request.destination = destination
            new_request.arrivalTime = arrivalTime
            new_request.NumPassanger = num
           
            new_request.CanShare = share
#            new_request.ownerEmail = request.session.get('user_email')
            new_request.status = 0
            new_request.save()
            return redirect('/request/')
            #return render(request,'rides/main.html')
    form = RideForm()
    return render(request, 'users/request.html', {'request_form':form})


def display_my_rides(request):
    requests = Ride.objects.all()
    print(requests)
    context = {"requests":requests}
    return render(request, "users/display.html", context=context)

def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")


def profile(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    email = request.session.get('user_email',False)
    print(email)
    users = haha.objects.filter(email=email).first()
    cars = car.objects.filter(driver_id = users)
 
    return render(request,'users/profile.html',{'users':users,'cars':cars})