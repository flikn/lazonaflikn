from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import MyUser


class UserSignupForm(forms.ModelForm):

    """A form for creating new users."""

    class Meta:
        model = MyUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
        ]

    def clean_password(self):
        # Check that the password min length is 6.
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise forms.ValidationError("Password min length is 6")
        elif len(password) > 255:
            raise forms.ValidationError("Password max length is 255")

        return password

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):

    """A form for login users."""

    email = forms.EmailField(
        max_length=50,
    )
    password = forms.CharField(
        max_length=100,
        min_length=6,
    )
