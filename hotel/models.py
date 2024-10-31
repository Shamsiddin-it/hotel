from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone = models.CharField( max_length=50)
    image = models.ImageField( upload_to="static/user/images")
    def __str__(self):
        return self.full_name

class Room(models.Model):
    ROOMS = (
        (1,"1"),
        (2,"2"),
        (3,"3")
    )
    CATEGORY = (
        ("simple","simple"),
        ("pro","pro"),
        ("lux","lux")
    )
    number = models.IntegerField()
    rooms = models.IntegerField(choices=ROOMS)
    category = models.CharField(choices=CATEGORY,max_length=50)
    image = models.ImageField(upload_to="static/room/images", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return f"room number {self.number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booked_on = models.DateField( auto_now=True)
    duration = models.CharField( max_length=50)

