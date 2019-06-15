from django.db import models

class Contacts(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'api'

    created = models.DateTimeField(auto_now_add=True)
    first = models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    email = models.EmailField(blank=False)
    number = models.CharField(max_length=15)
    message = models.CharField(max_length=15000)
    
    objects = models.Manager()

    def as_dict_response(self):
        return {
            "first": self.first,
            "last": self.last,
            "email": self.email,
            "number": self.number,
            "message": self.message
        }
