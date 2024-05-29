from django.urls import path

from.views import SettingsAPIVew

urlpatterns = [
    path('',SettingsAPIVew.as_view(), name='settings_api')
]