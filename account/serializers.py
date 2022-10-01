"""Personal information serializer"""
from rest_framework import serializers
from .models import (
    PersonInformation,
    Address
    )

class PersonInformationCreateSerializer(serializers.ModelSerializer):
    """serializer for Personal Information create"""
    class Meta:
        """override meta class"""
        model = PersonInformation
        fields = ['first_name', 'last_name', 'email', 'image', 'phone_number',
                  'bio', 'gender','address','created_at', 'updated_at']

class AddressCreateSerializer(serializers.ModelSerializer):
    """serializer for Address create"""
    class Meta:
        """override meta class"""
        model = Address
        fields = ['country', 'street', 'zip_code']

class AddressListSerializer(serializers.ModelSerializer):
    """serializer for Address create"""
    class Meta:
        """override meta class"""
        model = Address
        fields = ['id','country', 'street', 'zip_code']

class PersonInformationListSerializer(serializers.ModelSerializer):
    """serializer for Personal Information create"""
    address = AddressListSerializer(read_only=True)
    class Meta:
        """override meta class"""
        model = PersonInformation
        fields = ['id','first_name', 'last_name', 'email', 'image', 'phone_number',
                  'bio', 'gender','address','created_at', 'updated_at']
                  