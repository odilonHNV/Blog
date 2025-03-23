from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm

class UserProfilCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('email','username','password1','password2',)