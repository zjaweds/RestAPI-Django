from turtle import pd
from django.shortcuts import render
from .models import PassDetails, StudentDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import PassDetailsSerializer, StudentDetailsSerializer
# from QRCodeBackend.apis import serializers

# Create your views here.
StudentDetailsSchema = f'"id": "1","first_name": "Jawed","last_name": "Alam","email": "zjaweds@gmail.com","course": "MCA","roll_no": "19MCA020","student_image": "/media/uploads/2022/0622/1613544.jpg"'

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Student Details JSON Structure': StudentDetailsSchema,
        'Get A Student Detail: ':'unique-student-detail/{uid}',
        'Create a student Details':'create-student-details/',
        'Get All Student Details: ':'get-student-details/',
        'Delete Student Details':'delete-student-details/{st_Id}'
    }
    return Response(api_urls)

@api_view(['GET'])
def UniqueStudentDetails(request, st_Id):
    studentDetails = StudentDetails.objects.get(id = st_Id)
    serializer = StudentDetailsSerializer(studentDetails, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def GetStudentDetails(request):
    studentDetails = StudentDetails.objects.all()
    serializer = StudentDetailsSerializer(studentDetails, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateStudentDetails(request):
    serializer = StudentDetailsSerializer(data= request.data)
    if serializer.is_valid():
        print(serializer.validated_data)
        print("Serializer is Valid")
        serializer.save()
    else:
        print("Serializer is invalid")
        return Response(serializer.errors)    
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteStudentDetails(request, st_Id):
    pDetails = StudentDetails.objects.get(id = st_Id)
    pDetails.delete()
    return Response("Item Deleted Successfully")