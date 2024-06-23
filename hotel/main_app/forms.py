from django import forms

from main_app.models import HotelRoom, Booking


class RoomsForm(forms.ModelForm):
    class Meta:
        model = HotelRoom
        fields = '__all__'


class BookingsForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
