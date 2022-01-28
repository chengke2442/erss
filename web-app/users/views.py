from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm,CarForm,RideForm,LoginForm
from .models import haha,Ride, Relation
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
                new_car.driver_id = form.cleaned_data.get('email')
                new_car.vehicle_type =  form2.cleaned_data.get('vehicle_type')
                new_car.plate_number =  form2.cleaned_data.get('plate_number')
                                                              
                new_car.max_passanger =  form2.cleaned_data.get('max_passanger')
                new_car.save()
            return redirect('/login/')
    else:
        form = UserForm()
        form2 = CarForm()
    return render(request,'users/register.html',{'form':form,'car':form2})

def login(request):
#    if request.session.get('is_login',None):
#        return redirect('/login')    
#    if request.session.get('is_login',None):
#        return redirect('/login')
    
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "Please check what you have entered"
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            message = "Please enter correct information"
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
        
        return render(request, 'users/login.html', context={"message": message, 'login_form':login_form})
    else:
        login_form = LoginForm()
    return render(request,'users/login.html', {'login_form':login_form})

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
            #new_request = Ride.objects.create();
            new_request = Ride()            
            new_request.destination = destination
            new_request.arrivalTime = arrivalTime
            new_request.NumPassanger = num           
            new_request.CanShare = share
            new_request.owner_email = request.session.get('user_email')
            new_request.status = 0
            new_request.owner_id = request.session.get('user_id')
            new_request.save()

            # add to relation table
            new_relation = Relation()
            new_relation.r_request_id = new_request
            new_relation.r_owner_email = request.session.get('user_email')
            new_relation.save()
            
            return redirect('/display/')
            #return render(request,'rides/main.html')
    form = RideForm()
    return render(request, 'users/request.html', {'request_form':form})


def display_my_rides(request):
#    return HttpResponse("a display pagexxxxxx")
     requests = Ride.objects.filter(owner_email=request.session.get('user_email'))
     print(requests)
     context = {'requests':requests}
     return render(request, "users/display.html", context=context)

def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")
	
def addDriver(request):
    form2 = CarForm(request.POST)
    if form2.is_valid():
                h = request.session.get('user_id',None) 
                new_user = haha.objects.filter(id = h).first()
                new_user.status_flag = 1
                new_user.save()
                new_car = car.objects.create()
                new_car.driver_id = new_user
                new_car.vehicle_type =  form2.cleaned_data.get('vehicle_type')
                new_car.plate_number =  form2.cleaned_data.get('plate_number')
                                                              
                new_car.max_passanger =  form2.cleaned_data.get('max_passanger')
                new_car.save()
    return render(request,'users/newDriver.html',{'car':form2})

def profile(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    email = request.session.get('user_email',False)
    print(email)
    users = haha.objects.filter(email=email).first()
    cars = car.objects.filter(driver_id = users)
 
    return render(request,'users/profile.html',{'users':users,'cars':cars})

def rideDetail(request, request_id):
    response = "You're looking at the details of ride %s."
#    return HttpResponse(response % request_id)
    request_res = Ride.objects.get(pk=request_id)
    print(request_res)
    relation = Relation.objects.get(r_request_id=request_id)
    print(relation)
    driver_email = relation.r_driver_email;
    print(driver_email)
    driver = haha.objects.get(email=driver_email)
    print(driver.email)
    vehilce = car.objects.get(driver_id=driver_email)
    print(vehilce.plate_number)
    return render(request, 'users/rideDetail.html', {'request_id':request_res, 'driver':driver, 'car':vehilce})
 #   return HttpResponse(response % request_id)
