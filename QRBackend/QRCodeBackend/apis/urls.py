from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview' ),
    path('unique-student-detail/<str:st_Id>', views.UniqueStudentDetails, name='unique-student-details' ),
    path('create-student-details/', views.CreateStudentDetails, name='create-student-details' ),
    path('get-student-details/', views.GetStudentDetails, name='get-student-details' ),
    path('delete-student-details/<str:st_Id>', views.DeleteStudentDetails, name='delete-student-details' ),
]