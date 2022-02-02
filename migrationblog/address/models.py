from django.db import models

# Create your models here.
class AddressBook(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=25)
    address =  models.CharField(max_length=250, default='no address recorded')  # new column, default takes care of records from before without addressed 