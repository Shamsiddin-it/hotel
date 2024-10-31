from . models import *
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'age', 'email', 'phone', 'image')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('number', 'rooms', 'category', 'image')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'room', 'duration')

