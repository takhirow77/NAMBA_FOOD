from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .models import *
from .serializers import *


# Create your views here.
class ContactsAPIView(ListAPIView):
    queryset = Contacts.objects.all() # SELECT * FROM 
    serializer_class = ContactsSerializer

class ContactsAPICreate(CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class ContactsAPIRetrieve(RetrieveAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsDetailSerializer

class ContactsAPIUpdate(UpdateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsDetailSerializer

class ContactsAPIDestroy(DestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsDetailSerializer

