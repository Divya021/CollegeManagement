from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length=10,null=True)
    add = models.CharField(max_length=100,null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.user.first_name



class Add_Bus(models.Model):
    busname = models.CharField(max_length=30,null=True)
    bus_no = models.CharField(max_length=30,null=True)
    from_city = models.CharField(max_length=30,null=True)
    to_city = models.CharField(max_length=30,null=True)
    departuretime=models.CharField(max_length=30,null=True)
    arrivaltime=models.CharField(max_length=30,null=True)
    trevaltime=models.CharField(max_length=100,null=True)
    distance=models.IntegerField(null=True)
    img=models.FileField(null=True)
    def __str__(self):
        return self.busname+" "+str(self.bus_no)

class Add_route(models.Model):
    bus = models.ForeignKey(Add_Bus,on_delete=models.CASCADE,null=True)
    route = models.CharField(max_length=30,null=True)
    distance=models.IntegerField(null=True)
    fare=models.IntegerField(null=True)
    def __str__(self):
        return self.route+" "+self.bus.busname+" "+str(self.bus.bus_no)
class Book_ticket(models.Model):
    user=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    route=models.ForeignKey(Add_route,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    passenger=models.IntegerField(null=True)
    def __str__(self):
        return self.user.username+" "+self.route.route




