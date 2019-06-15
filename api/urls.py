from django.urls import path
from api.views import ContactsCreateView

urlpatterns = [
    path('api/v1/contact/create', ContactsCreateView.as_view({'post': 'create'}), name='contact-create-view')
]
