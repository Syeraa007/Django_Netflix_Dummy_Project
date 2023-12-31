from django import forms
from App.models import *

class Users(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}
        
class Profiles(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','picture']