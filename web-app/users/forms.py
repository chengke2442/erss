from django import forms
from .models import haha,Ride
from .models import car
from django.forms import DateTimeField


class UserForm(forms.Form):
    status = {('1',"I want to be a driver" ),('0',"I don't want to be a driver")}
    first_name = forms.CharField(label="First Name",max_length = 30,widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Last Name",max_length = 30,widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label = "Password",max_length = 256,widget = forms.PasswordInput(attrs={'class':'form-control'}),required = False)
    password2 =  forms.CharField(label = "Comfirm Password",max_length = 256,widget = forms.PasswordInput(attrs={'class':'form-control'}),required = False)         
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label="Phone Number",max_length = 100,widget = forms.TextInput(attrs={'class':'form-control'}))
    status_flag = forms.ChoiceField(label = "Would like to be a driver?",choices = status,required=False )
    vehicle_id = forms.CharField(label="Vehicle id",max_length=10,required = False)      
    class Meta:
        model = haha

class CarForm(forms.Form):
    carType = {('1',"Sedan" ),('0',"SUV"),('2',"Wagon"),('3',"HatchBack"),('4',"Truck")}
    passanger={("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8")}
    #driver_id = models.ForeignKey('haha',on_delete=models.CASCADE,blank=True,null=True)
    vehicle_type = forms.ChoiceField(label="Please choose your vehicle type",choices = carType)
    plate_number = forms.CharField(label="Please Enter your plate Number",max_length=10)
    max_passanger = forms.ChoiceField(label="Please Choose Maximum Passanger",choices = passanger)
    class Meta:
        model = car



class RideForm(forms.Form):
    status = {(0,"Yes" ),(1,"No")}
    destination  = forms.CharField(label="Your destination", max_length = 20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #arrivalTime = forms.DateField(label='Arrival Time', widget=forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'type':'date'}))
    arrivalTime = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'], widget = forms.DateTimeInput(attrs={'type': 'datetime-local'},format='%I:%M %p %d-%b-%Y')) 
    NumPassanger = forms.IntegerField(label="The number of passager in this ride:", min_value=1)
    CanShare = forms.ChoiceField(label="Would you like to share your ride with others?", choices=status)
    #TODO add vechile type
    class Meta:
        model = Ride

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = "Password",max_length = 256,widget = forms.PasswordInput())
    class Meta:
        model = haha


class editDestinationForm(forms.Form):
    destination  = forms.CharField(label="Your destination", max_length = 20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Ride


class editTimeForm(forms.Form):
    arrivalTime = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'], widget = forms.DateTimeInput(attrs={'type': 'datetime-local'},format='%I:%M %p %d-%b-%Y'))
    class Meta:
        model = Ride


class editNumForm(forms.Form):
    num = forms.IntegerField(label="The number of passager in this ride:", min_value=1)
    class Meta:
        model = Ride

class editShareForm(forms.Form):
    status = {(0,"Yes" ),(1,"No")}
    CanShare = forms.ChoiceField(label="Would you like to share your ride with others?", choices=status)
    class Meta:
        model = Ride
