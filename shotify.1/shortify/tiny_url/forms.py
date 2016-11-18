from django import forms
from django.contrib.auth.models import User
from tiny_url.models import UserProfile, Url



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class ShortUrlForm(forms.ModelForm):
    full_url=forms.URLField(max_length=200)
    
    
    class Meta:
        model = Url
        fields = ('full_url',)
        
"""class LongUrlForm(forms.ModelForm):
    short_code=forms.CharField(max_length=6)
    
    class Meta:
        model=Url
        fields=('short_code')"""