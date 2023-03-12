from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'role', 'country', 'nationality', 'phone_number', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
