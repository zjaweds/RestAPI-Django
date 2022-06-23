from django.contrib import admin
from .models import StudentDetails
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
  list_display = ['id','first_name','last_name','email','course','roll_no','student_image']
admin.site.register(StudentDetails, StudentAdmin)