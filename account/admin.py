import imp
from django.contrib import admin
from .models import Address,PersonInformation

admin.site.register(Address)
admin.site.register(PersonInformation)
