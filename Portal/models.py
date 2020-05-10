from django.db import models
from datetime import datetime


class User(models.Model):
    user_id=models.PositiveIntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField(max_length=50)
    approved_field= models.BooleanField()
    add1 = models.CharField(max_length=50)
    add2 =models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    zip= models.PositiveIntegerField()
    county= models.CharField(max_length=50)
    signed_on= models.DateTimeField()
    can_flag_connect= models.BooleanField()
    tutor_flag = models.BooleanField()
    tutor_flag_date=models.DateTimeField(default=datetime.now)
    volunteer_flag_date=models.DateTimeField(default=datetime.now)
    list_on_wish_flag=models.BooleanField()
    list_on_wish_flag_date=models.DateTimeField()

    def __str__(self):
        return self.orgname


class Volunteer_Work(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # it will delete all the objects related to this field
    description = models.CharField(max_length=200)
    hours = models.PositiveIntegerField()
    date_time = models.DateTimeField()
    proof = models.FileField(upload_to='files/', null=False)
    share_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.service_name

class Organization(models.Model):
    org_id = models.PositiveIntegerField(primary_key=True)
    orgname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    approved_field = models.BooleanField()
    add1 = models.CharField(max_length=50)
    add2 = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.PositiveIntegerField()
    county = models.CharField(max_length=50)
    signed_on = models.DateTimeField()
    volunteer_flag_date = models.DateTimeField(default= datetime.now)
    list_on_wish_flag = models.BooleanField()
    list_on_wish_flag_date = models.DateTimeField()

    def __str__(self):
        return self.orgname


class Services(models.Model):
    service_id = models.PositiveIntegerField(primary_key=True)
    service_name = models.CharField(max_length=200)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.service_name



