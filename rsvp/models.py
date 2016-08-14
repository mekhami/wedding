from django.db import models


# Create your models here.
class RSVP(models.Model):
    name = models.CharField(max_length=256)
    address1 = models.CharField(max_length=256)
    address2 = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=8)
    email = models.EmailField()
    song_request = models.CharField(max_length=256, null=True, blank=True)
    guests = models.IntegerField()
    attending = models.BooleanField()

    def __str__(self):
        return self.name
