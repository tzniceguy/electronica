from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class CustomUSerCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    phonenumber = forms.IntegerField(required = True,
                                     widget=forms.NumberInput(attrs={'placeholder':
                                                                     'PhoneNumber(255)', 'class':
                                                                      'form-control', }))
    password1 = forms.CharField(max_length=50,
                                label='Password',
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                label='Repeat Password',
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phonenumber', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    phonenumber =forms.CharField(required=False,
                                   widget =forms.NumberInput(attrs={'class': 'form-control'}))
    profile_image =forms.ImageField(required=False,
                                    widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = CustomUser
        fields = ['profile_image','username', 'email', 'phonenumber']