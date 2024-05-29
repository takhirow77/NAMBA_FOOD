from django.shortcuts import render
from rest_framework.generics import ListAPIView

from.models import Settings
from.serializers import SettingsSerializers

# Create your views here.

class SettingsAPIVew(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializers