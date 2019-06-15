from django.urls import path
from api.views import ContactsCreateView

urlpatterns = [
    path('api/v1/contact/create', ContactsCreateView.as_view(), name='contact-create-view')
]
