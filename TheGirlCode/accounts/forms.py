from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)  # Valid email is mandatory

    class Meta:  # Description of the form
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):  # Saves the data to the data base
        user = super(RegistrationForm, self ).save(commit=False)
        user.email = self.cleaned_data['email']  # Checks for code that can harm the site in the input box

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:  # Description of the form
        model = User
        fields = (
            'username',
            'email',
            'password',
        )


