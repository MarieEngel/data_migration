from django.contrib import admin
from . import  models
# Register your models here.
class AddressBookAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.AddressBook, AddressBookAdmin)


