"""Views For Personal Informations"""
from django.shortcuts import render
from rest_framework import generics
from .models import PersonInformation,Address
from .serializers import (
    PersonInformationCreateSerializer,
    PersonInformationListSerializer,
    AddressCreateSerializer,
    AddressListSerializer
)
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAdminUser, AllowAny

class PersonInformationListView(generics.ListAPIView):
    """View to list Person Information"""
    queryset = PersonInformation.objects.all()
    serializer_class = PersonInformationListSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['first_name', 'last_name', 'email','phone_number','bio', 'gender','address']
    ordering_fields = ['first_name', 'last_name', 'email']
    filterset_fields = {
        'first_name':['exact'],'last_name':['exact'],'email':['exact'],'gender':['exact']
    }

class PersonInformationCreateView(generics.CreateAPIView):
    """View to create Person Information"""

    queryset = PersonInformation.objects.all()
    serializer_class = PersonInformationCreateSerializer
    # permission_classes = [IsAdminUser]

    def post(self, request):
        """This method is used to create state"""
        person_information_serializer = PersonInformationCreateSerializer(data=request.data)
        print(request.data)
        if person_information_serializer.is_valid():
            person_information_serializer.save()
            return Response(person_information_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(person_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonInformationDetailView(generics.RetrieveAPIView):
    """View to show detail of Personal Information"""

    queryset = PersonInformation.objects.all()
    serializer_class = PersonInformationListSerializer
    lookup_field = 'pk'

class PersonInformationUpdateView(generics.RetrieveUpdateAPIView):

    """View to update Personal Information"""

    queryset =PersonInformation.objects.all()
    serializer_class = PersonInformationCreateSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class PersonInformationDeleteView(generics.RetrieveDestroyAPIView):
    """View to delete Personal Information"""

    queryset = PersonInformation.objects.all()
    serializer_class = PersonInformationListSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class AddressListView(generics.ListAPIView):
    """View to list Address Information"""
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['country', 'street', 'zip_code']
    ordering_fields = ['country']
    filterset_fields = {
        'country':['exact'],'street':['exact'],'zip_code':['exact']
    }

class AddressCreateView(generics.CreateAPIView):
    """View to create Address Information"""

    queryset = Address.objects.all()
    serializer_class = AddressCreateSerializer
    # permission_classes = [IsAdminUser]

    def post(self, request):
        """This method is used to create state"""
        address_serializer = AddressCreateSerializer(data=request.data)
        print(request.data)
        if address_serializer.is_valid():
            address_serializer.save()
            return Response(address_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressDetailView(generics.RetrieveAPIView):
    """View to show detail of Address Information"""

    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
    lookup_field = 'pk'

class AddressUpdateView(generics.RetrieveUpdateAPIView):

    """View to update Address Information"""

    queryset =Address.objects.all()
    serializer_class = AddressCreateSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class AddressDeleteView(generics.RetrieveDestroyAPIView):
    """View to delete Address Information"""

    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'pk'