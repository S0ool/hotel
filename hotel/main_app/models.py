from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class HotelRoom(models.Model):
    room_type = models.CharField(max_length=100)
    room_number = models.IntegerField(unique=True)
    room_price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to=f'%d-%m-%y')

    def __str__(self):
        return str(self.room_number)


class Booking(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.guest.username
