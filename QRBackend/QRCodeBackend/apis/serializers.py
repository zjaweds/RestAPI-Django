from rest_framework import serializers
from .models import PassDetails, StudentDetails

class PassDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassDetails
        fields ='__all__'

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields ='__all__'
