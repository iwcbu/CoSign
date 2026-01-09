# cosign/forms.py

from django import forms
from .models import *

#       Forms are 

class CreateProfileForm(forms.ModelForm):
    '''form to create a profile'''

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'username',
            'bio',
            'pfp_file'
        ]

class UpdateProfileForm(forms.ModelForm):
    '''form to update a profile'''

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'username',
            'bio',
            'pfp_file'
        ]

