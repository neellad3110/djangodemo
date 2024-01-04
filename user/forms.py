from typing import Any
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
 

class user_registration_form(UserCreationForm):     #custom form class


    # email = forms.EmailField(validators=[EmailValidator(message='Enter a valid email address.')])
    email = forms.EmailField(required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already in use.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2    
    

class user_authentication_form(forms.Form):     #custom form class


    username_or_email = forms.CharField()
    password=forms.CharField()
   
    def clean_username_or_email(self):
        username_or_email = self.cleaned_data["username_or_email"]
        return username_or_email

    def clean_password(self):
        password = self.cleaned_data["password"]
        return password
        


