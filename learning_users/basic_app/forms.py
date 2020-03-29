from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# the base form:
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
        # Here we could also ask also for first and last names!


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
