from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from petstagram.accounts.models import PetstagramUser


class PetstagramUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PetstagramUser
        fields = ('username', 'email')

    # instead of custom_filters.py/placeholder

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['placeholder'] = 'Username'
    #     self.fields['email'].widget.attrs['placeholder'] = 'Email'
    #     self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Repeat password'


class PetstagramUserEditForm(forms.ModelForm):
    class Meta:
        model = PetstagramUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender')
        exclude = ('password',)
        labels = {
            'username': 'Username:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'profile_picture': 'Image:',
            'gender': 'Gender:',
        }


class LoginForm(AuthenticationForm):
    pass
