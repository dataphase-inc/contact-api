from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models import Contacts
from api.serializers import ContactsSerializer
import smtplib
class ContactsCreateView(viewsets.ViewSet):
    def create(self, request):
        serializer = ContactsSerializer(request.data)
        if serializer.is_valid:
            serializer.create(serializer.data)

            gmail_user = 'contactapidataphaase@gmail.com'  
            gmail_password = '123asdqwe'

            sent_from = gmail_user  
            to = 'admin@dataphase.io'
            subject = 'IMPORTANT! | Client Prospect'  
            body = serializer.data

            email_text = """
            From: %s  
            To: %s  
            Subject: %s

            %s
            """ % (sent_from, to, subject, body)

            try:  

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, email_text)
                server.close()

                print('Email sent!')
            except:  
                print('Something went wrong...')
            return Response({'enter': 'success'}, status.HTTP_200_OK)
        else:
            return Response({'enter': 'failure'}, status.HTTP_400_BAD_REQUEST)

