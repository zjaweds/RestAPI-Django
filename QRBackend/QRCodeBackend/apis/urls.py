from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.apiOverview, name='api-overview' ),
    path('all-pass-details/', views.AllPassDetails, name='all-pass-details' ),
    path('unique-pass-details/<str:payment_Id>', views.UniquePassDetails, name='unique-pass-details' ),
    path('create-pass-details/', views.CreatePassDetails, name='create-pass-details' ),
    path('update-pass-details/<str:payment_Id>', views.UpdatePassDetails, name='update-pass-details' ),
    path('delete-pass-details/<str:payment_Id>', views.DeletePassDetails, name='delete-pass-details' ),
]

