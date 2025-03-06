from .models import bookings
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = bookings
        fields = "__all__"
    