from django.db import models

# Create your models here.

class Customer(models.Model):
    #主键
    customerID = models.CharField(primary_key=True, max_length=12)


    image = models.ImageField(width_field=100,height_field=100)
    name = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    ID_number = models.CharField(max_length=20)
    birthdate = models.DateField()
    province =  models.CharField(max_length=20)
    city =  models.CharField(max_length=20)
    area =  models.CharField(max_length=20)
    address =  models.CharField(max_length=40)
    marrige =  models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    height =  models.FloatField()
    weight =  models.FloatField()
    remark =  models.TextField()
    phonenum1 = models.CharField(max_length=11)
    phonenum2 =  models.CharField(max_length=11)
    check_in_date =  models.DateField()
    check_out_date =  models.DateField()
    state_1 =  models.BooleanField()
    state_2 =  models.BooleanField()

    bedID =  models.ForeignKey('Bed' , to_field='bedID', default=1, on_delete=models.CASCADE)
    #staffID =  models.ForeignKey(primary_key=True, max_length=10)


class Bed(models.Model):
    #主键
    bedID = models.CharField(primary_key=True, max_length=10)