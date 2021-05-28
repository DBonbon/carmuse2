from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #todo override help_text in UserCreationForm
        # todo check: https://stackoverflow.com/questions/61306006/how-to-override-help-text-and-label-for-password-form-in-django?noredirect=1&lq=1
        """
        help_texts = {
            'username': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
            'password1': 'Your password can’t be too similar to your other personal information.',
        }

        def __init__(self, *args, **kwargs):
            super(UserRegisterForm, self).__init__(*args, **kwargs)
            self.fields['username'].help_text = 'At leasst 8 characters Letters, digits and @/./+/-/_ only'
            self.fields['password1'].help_text = 'Your password must contain at least one digit and one character'
"""

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
