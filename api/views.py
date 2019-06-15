from rest_framework import generics
from api.models import Contacts
from api.serializers import ContactsSerializer

class ContactsCreateView(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer