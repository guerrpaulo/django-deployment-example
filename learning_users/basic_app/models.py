from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # the actual model. something that expands of that user! He inherit it from 'models.Model'.

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # this is one-to-one match with the built in User from django!
    # this includes already the following user atributes: Username, Email, Password, First Name, Surname

    # Now we Add any additional attributes you want:
    portfolio_site = models.URLField(blank=True)   # this means the user don't have to fill it out. its optional.
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
