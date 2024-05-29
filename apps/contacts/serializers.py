from rest_framework import serializers

from .models import *


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'description', 'phone_number']


class ContactsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'