from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CustomUSerCreationForm(UserCreationForm):
    email = forms.EmailField()
    phonenumber = forms.IntegerField(label='Phone Number(255)')

    class Meta:
        model =User
        fields= ['username', 'email', 'phonenumber', 'password1', 'password2']
        widgets = {
            'phonenumber': forms.TextInput(attrs={'placeholder': 'format: (+255)'}),
            'dob': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }