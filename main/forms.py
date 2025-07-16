from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from typing import Any


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].widgets.attrs["class"] = 'form-control',
        self.fields["username"].widgets.attrs["placeholder"] = 'Your Username',
        self.fields["email"].widgets.attrs["class"] = 'form-control',
        self.fields["email"].widgets.attrs["placeholder"] = 'Your Email',
        self.fields["password1"].widgets.attrs["class"] = 'form-control',
        self.fields["password1"].widgets.attrs["placeholder"] = 'Your password',
        self.fields["password2"].widgets.attrs["class"] = 'form-control',
        self.fields["password2"].widgets.attrs["placeholder"] = 'Confirm password'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widgets.attrs["class"] = 'form-control',
        self.fields["password"].widgets.attrs["class"] = 'form-control'
        