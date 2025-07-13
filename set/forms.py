from django import forms
from .models import Reservation,MenuItem

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class MenuItemForm(forms.ModelForm):
    
    class Meta:
        model = MenuItem
        fields = '__all__'
