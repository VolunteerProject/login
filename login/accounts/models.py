from django.db import models
from datetime import datetime

class User(models.Model):
    USER_ID=models.PositiveIntegerField(primary_key=True)
    FIRST_NAME=models.CharField(max_length=100)
    LAST_NAME = models.CharField(max_length=100)
    EMAIL=models.EmailField(max_length=50)
    APPROVED_FIELD=models.BooleanField()
    ADD1=models.CharField(max_length=50)
    ADD2=models.CharField(max_length=50)
    COUNTRY=models.CharField(max_length=50)
    STATE = models.CharField(max_length=50)
    CITY = models.CharField(max_length=50)
    ZIP= models.PositiveIntegerField()
    COUNTY = models.CharField(max_length=50)
    SIGNED_ON= models.DateTimeField()
    CAN_CONNECT_FLAG= models.BooleanField()
    TUTOR_FLAG = models.BooleanField()
    TUTOR_FLAG_DATE=models.DateTimeField(default=datetime.now)
    VOLUNTEER_FLAG_DATE=models.DateTimeField(default=datetime.now)
    LIST_ON_WISH_FLAG=models.BooleanField()
    LIST_ON_WISH_FLAG_DATE=models.DateTimeField()


class Organization(models.Model):
    ORG_ID = models.PositiveIntegerField(primary_key=True)
    ORGNAME = models.CharField(max_length=100)
    EMAIL = models.EmailField(max_length=50)
    APPROVED_FIELD = models.BooleanField()
    ADD1 = models.CharField(max_length=50)
    ADD2 = models.CharField(max_length=50)
    COUNTRY = models.CharField(max_length=50)
    STATE = models.CharField(max_length=50)
    CITY = models.CharField(max_length=50)
    ZIP = models.PositiveIntegerField()
    COUNTY = models.CharField(max_length=50)
    SIGNED_ON = models.DateTimeField()
    VOLUNTEER_FLAG_DATE = models.DateTimeField(default= datetime.now)
    LIST_ON_WISH_FLAG = models.BooleanField()
    LIST_ON_WISH_FLAG_DATE = models.DateTimeField()


class Volunteer_Work(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    USER_ID=models.ForeignKey(User,on_delete=models.CASCADE) # it will delete all the objects related to this field
    DESCRIPTION=models.CharField(max_length=200)
    HOURS=models.PositiveIntegerField()
    DATETIME=models.DateTimeField()
    PROOF=models.FileField(upload_to='files/',null=False)
    SHARE_EMAIL=models.EmailField(max_length=50)

class Services(models.Model):
    SERVICE_ID=models.PositiveIntegerField(primary_key=True)
    SERVICE_NAME=models.CharField(max_length=200)
    ORGANIZATION_ID=models.ForeignKey(Organization,on_delete=models.CASCADE,null=True,blank=True )
    USER_ID=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.SERVICE_NAME

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'