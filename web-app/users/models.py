from django.db import models
from django.utils import timezone

class haha(models.Model):
        #delete username
        first_name = models.CharField(max_length=30);
        last_name = models.CharField(max_length=30);
        email = models.EmailField(unique=True)
        password = models.CharField(max_length=200)
        status = {('1',"I want to be a driver" ),('0',"I don't want to be a driver")}
        # add some text
        phone_number = models.CharField(max_length = 100);
        status_flag = models.CharField(max_length = 1);
        vehicle_id = models.CharField(max_length = 10,unique=True, null=True);

        def  __str__(self):
                return self.last_name
       
                           
               
# Create your models here.

class car(models.Model):

    driver_id = models.ForeignKey('haha',on_delete=models.CASCADE,blank=True,null=True)
    vehicle_type = models.CharField(default="Sedan",max_length=10)
    plate_number = models.CharField(max_length=10, default="test")
    max_passanger = models.CharField(default="4",max_length=1)

'''    
class Ride(models.Model):
        destination = models.CharField(max_length=30);
        arrivaltime = models.DateTimeField(default = timezone.now());
        NumPassanger = models.IntegerField();
        CanShare = models.IntegerField();
        #ownerEmail = models.CharField(max_length=200);
        max_passanger = models.IntegerField(null=True);
        status = models.IntegerField(default=0);
'''

class Ride(models.Model):
        destination = models.CharField(max_length=30);
        arrivaltime = models.DateTimeField(default = timezone.now());
        NumPassanger = models.IntegerField();
        CanShare = models.IntegerField();
        owner_id = models.IntegerField(null=True);
        #    owner_id = models.ForeignKey('haha', on_delete=models.CASCADE);
        max_passanger = models.IntegerField(null=True);
        status = models.IntegerField(default=0);
        owner_email = models.EmailField(null=True);

class Relation(models.Model):
        r_request_id = models.ForeignKey('Ride', on_delete=models.CASCADE);
        r_driver_id = models.ForeignKey('haha',related_name='%(class)s_user_dirver', on_delete=models.CASCADE, null=True);
#        r_owner_id = models.ForeignKey('haha', related_name='%(class)s_user_owner', on_delete=models.CASCADE);
        r_owner_id = models.IntegerField(); 
        r_sharer_id = models.ForeignKey('haha', related_name='%(class)s_user_sharer', on_delete=models.CASCADE, null=True);
