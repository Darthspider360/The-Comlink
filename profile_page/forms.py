from django import forms
from .models import Profile

class Profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('rank', 'profile_image', 'bio',)