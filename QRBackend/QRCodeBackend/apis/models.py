import email
import os
from django.db import models
from django.forms import ValidationError
# Create your models here.

def validate_file_extension(value):
    print("Value: "+str(type(value)))
    valid_file_extensions = ['.jpg','.png','.jpeg']
    try:
        if value.file.content_type != 'application/jpg':
            raise ValidationError(u'Upload an image')
    except:
        ext = os.path.splitext(value.name)[1]
        if ext.lower() not in valid_file_extensions:
            raise ValidationError('Unacceptable file extension.')

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


class StudentDetails(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    first_name = models.CharField(max_length=20, unique=False)
    last_name = models.CharField(max_length=30, unique=False)
    email = models.EmailField(blank=False)
    course = models.CharField(max_length=30, unique=False)
    roll_no = models.CharField(max_length=30, unique=True)
    student_image = models.ImageField(upload_to='uploads/%Y/%m%d/', blank=True, verbose_name='Upload Image')
    
    def __str__(self):
        return str(self.first_name)