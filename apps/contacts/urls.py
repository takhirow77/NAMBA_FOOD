from django.urls import path

from .views import *

urlpatterns = [
    path('', ContactsAPIView.as_view(), name='Contacts_api'),
    path('create/', ContactsAPICreate.as_view(), name='contacts_create_api'),
    path('<int:pk>/', ContactsAPIRetrieve.as_view(), name='contacts_retrieve_api'),
    path('update/<int:pk>/', ContactsAPIUpdate.as_view(), name='contacts_update_api'),
    path('destroy/<int:pk>/', ContactsAPIDestroy.as_view(), name='contacts_destroy_api'),
]