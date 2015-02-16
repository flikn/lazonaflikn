from django import forms
from django.core import validators
from .models import MyUser


class UserSignupForm(forms.ModelForm):

    """A form for creating new users."""
    username = forms.CharField(
        required=False,
    )

    class Meta:
        model = MyUser
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
        ]

    def clean_password(self):
        # Check that the password min length is 6.
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise forms.ValidationError("Password min length is 6")
        elif len(password) > 255:
            raise forms.ValidationError("Password max length is 255")
        return password

    def name_is_not_empty(self, raw_name):
        name = " ".join(raw_name.split())
        if not name:
            raise forms.ValidationError("Name cannot be left empty")
        return name

    def clean_first_name(self):
        first_name = self.name_is_not_empty(
            self.cleaned_data.get("first_name")
        )
        first_name = first_name.split()[0].title()
        return first_name

    def clean_last_name(self):
        last_name = self.name_is_not_empty(self.cleaned_data.get("last_name"))
        last_name = last_name.title()
        return last_name

    def save(self, commit=True):
        user = super(UserSignupForm, self).save(commit=False)
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


class RequiredExtraDataForm(forms.Form):

    """A form for require extra data through the pipeline."""

    email = forms.EmailField(
        max_length=50,
        required=False,
    )
    first_name = forms.CharField(
        max_length=50,
        validators=[
            validators.RegexValidator(
                r"^[a-zA-Z ]",
                "Invalid name."
            ),
        ],
        required=False,
    )
    last_name = forms.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator(
                r"^[a-zA-Z ]",
                "Invalid name."
            ),
        ],
        required=False,
    )
    password = forms.CharField(
        max_length=255,
        min_length=6,
        required=False,
    )

    def name_is_not_empty(self, raw_name):
        name = " ".join(raw_name.split())
        if not name:
            raise forms.ValidationError("Name cannot be left empty")
        return name

    def clean_first_name(self):
        first_name = self.name_is_not_empty(
            self.cleaned_data.get("first_name")
        )
        first_name = first_name.split()[0].title()
        return first_name

    def clean_last_name(self):
        last_name = self.name_is_not_empty(self.cleaned_data.get("last_name"))
        last_name = last_name.title()
        return last_name

    def clean_email(self):
        email = self.cleaned_data['email']
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
