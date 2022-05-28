from dataclasses import fields
from rest_framework import serializers
from .models import PassDetails

class PassDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassDetails
        fields ='__all__'
