from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone', 'persons']

   

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'persons': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
        }

    def clean_persons(self):
        persons = self.cleaned_data.get('persons')
        if persons < 1:
            raise forms.ValidationError("At least one person is required.")
        return persons
