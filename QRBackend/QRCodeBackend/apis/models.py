import email
from django.db import models
# Create your models here.

class PassDetails(models.Model):
    event = models.CharField(max_length=40, unique=False)
    pass_type = models.CharField(max_length=20, unique=False)
    item_count = models.BigIntegerField()
    full_name = models.CharField(max_length=30, unique=False)
    phone = models.BigIntegerField()
    email = models.EmailField(blank=False)
    payment_Id = models.CharField(max_length=30, unique=True)
    redeem_status = models.BooleanField(default=False, unique=False)
    
    def __str__(self):
        return str(self.full_name)
#    Event	Item Name	Item Quantity	Full Name	Phone	Email	payment id (QR)
# DelhiKop UCL Final Mega Screening	Limited Pass	2	Varun Naik	9035770942	varun.naik39@gmail.com	pay_JVVbms8ka5AtSp
