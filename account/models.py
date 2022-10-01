"""this module is for person and address information model"""
from django.db import models


class Address (models.Model):
    """this model is for address of user"""
    country = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    zip_code = models.IntegerField(null=True,blank=True)
    class Meta:
        """override meta class"""
        verbose_name = 'Address'
        verbose_name_plural = 'Address'

    def __str__(self):
        """It represent object in string format, it shows address"""
        return self.country

class Status(models.TextChoices):
    '''choices for status'''
    Male = 'Male','Male'
    Female = 'Female','Female'
    Others = 'Others','Others'

class PersonInformation(models.Model):
    '''this model is for personal information of user'''
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    gender = models.CharField(max_length=10,choices=Status.choices,default=Status.Male)
    address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name = "user_address")
    image = models.ImageField(upload_to='user/image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        """override meta class"""
        verbose_name = 'Personal Information'
        verbose_name_plural = 'Personal Informations'

    def __str__(self):
        """It represent object in string format, it shows email"""
        return self.email
