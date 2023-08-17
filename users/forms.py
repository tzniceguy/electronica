from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class CustomUSerCreationForm(UserCreationForm):
    email = forms.EmailField()
    phonenumber = forms.IntegerField(label='Phone Number(255)')

    class Meta:
        model =CustomUser
        fields= ['username', 'email', 'phonenumber', 'password1', 'password2']
        widgets = {
            'phonenumber': forms.TextInput(attrs={'placeholder': 'format: (+255)'}),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }

