from django.contrib import admin
from.models import *

# Register your models here.
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'email']
    list_filter = ['id', 'description', 'email', 'phone_number']