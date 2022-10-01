"""url of team management"""
from django.urls import path
from . import views

urlpatterns = [
    # Personal Information endpoints
    path('person/', views.PersonInformationListView.as_view()),
    path('person-create/', views.PersonInformationCreateView.as_view()),
    path('person-detail/<int:pk>/', views.PersonInformationDetailView.as_view()),
    path('person-update/<int:pk>/', views.PersonInformationUpdateView.as_view()),
    path('person-delete/<int:pk>/', views.PersonInformationDeleteView.as_view()),
    # Address Information endpoints
    path('address/', views.AddressListView.as_view()),
    path('address-create/', views.AddressCreateView.as_view()),
    path('address-detail/<int:pk>/', views.AddressDetailView.as_view()),
    path('address-update/<int:pk>/', views.AddressUpdateView.as_view()),
    path('address-delete/<int:pk>/', views.AddressDeleteView.as_view()),
]