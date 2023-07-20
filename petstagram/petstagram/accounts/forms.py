from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from petstagram.accounts.models import PetstagramUser

UserModel = get_user_model()


class PetstagramUserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
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
        model = UserModel
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile_picture',
            'gender'
        )
        exclude = ('password',)
        labels = {
            'username': 'Username:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'profile_picture': 'Image:',
            'gender': 'Gender:',
        }


class LoginForm(auth_forms.AuthenticationForm):
    pass
