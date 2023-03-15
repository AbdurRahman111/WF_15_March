from rest_framework import serializers
from datetime import datetime

class User_information_serializer(serializers.Serializer):
    # User_Roll_CHOICES = (
    #     ('Admin', 'Admin'),
    #     ('Manager', 'Manager'),
    #     ('Operations', 'Operations'),
    #     ('Data Entry', 'Data Entry'),
    #     ('Normal User', 'Normal User'),
    # )
    # User_Roll = serializers.CharField(max_length=256, choices=User_Roll_CHOICES, blank=True, null=True)
    id = serializers.ReadOnlyField()
    User_Roll = serializers.CharField(max_length=256)

    User_Name = serializers.CharField(max_length=256)
    User_Password = serializers.CharField(max_length=256)
    User_Email = serializers.CharField(max_length=256)
    User_Phone = serializers.CharField(max_length=256)
    User_Joing_Date_Time = serializers.DateTimeField(default=datetime.now())

class find_manager_information_serializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    User_Roll = serializers.CharField(max_length=256)
    User_Email = serializers.CharField(max_length=256)
    User_Phone = serializers.CharField(max_length=256)
    User_Joing_Date_Time = serializers.DateTimeField(default=datetime.now())