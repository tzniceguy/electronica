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
            'phonenumber': forms.TextInput(attrs={'placeholder': 'format: (+255)', 'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    password = forms.PasswordInput(attrs={'class': 'form-control'})

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']