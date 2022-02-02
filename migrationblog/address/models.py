from django.db import models

# Create your models here.
class AddressBook(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=25)
    # 8) remove address field, makemigrations, migrate:
    # address =  models.CharField(max_length=250, default='no address recorded')  # 0) new column, default takes care of records from before without addressed 
    #  to save postal code from address field to new field 'postcode' and get rid of address field:
    # 1) create new field, makemigration, 
   
    postcode = models.CharField(max_length=15, default = "00000")
    # 2) to get postal code from address: data migration: makemigrations --empty address -> rename migration file
    # 3) -> migration file
    