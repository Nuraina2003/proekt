from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

User = get_user_model()

from .models import Registration


class AddPostForm(forms.ModelForm):
    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].empty_label = "Таңдаңыз"

    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Registration
        fields = '__all__'

class LoginUserForm(AuthenticationForm):
        username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


