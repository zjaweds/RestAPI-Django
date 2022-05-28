from turtle import pd
from django.shortcuts import render
from .models import PassDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import PassDetailsSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Get All Pass Details: ':'all-pass-details/',
        'Get One Pass Detail: ':'unique-pass-details/{uid}',
        'Update A Pass Detail: ':'update-pass-details/{uid}',
        'Delete A Pass Detail: ':'delete-pass-details/{uid}',
    }
    return Response(api_urls)

@api_view(['GET'])
def AllPassDetails(request):
    pDetails = PassDetails.objects.all()
    serializer = PassDetailsSerializer(pDetails, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UniquePassDetails(request, payment_Id):
    pDetails = PassDetails.objects.get(payment_Id = payment_Id)
    serializer = PassDetailsSerializer(pDetails, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreatePassDetails(request):
    serializer = PassDetailsSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def UpdatePassDetails(request, payment_Id):
    pDetails = PassDetails.objects.get(payment_Id = payment_Id)
    pDetails.redeem_status= request.data['redeem_status']
    # print(pDetails)
    # print(serializer.is_valid())
    # if serializer.is_valid():
    # print(serializer.data)
    pDetails.save()
    serializer = PassDetailsSerializer(instance = pDetails)
    # serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeletePassDetails(request, payment_Id):
    pDetails = PassDetails.objects.get(payment_Id = payment_Id)
    pDetails.delete()
    return Response("Item Deleted Successfully")