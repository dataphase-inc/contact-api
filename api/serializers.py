
from rest_framework import serializers
from api.models import Contacts

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = [
            'first',
            'last',
            'email',
            'number',
            'message'
        ]

    def create(self, validated_data):
        return Contacts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated