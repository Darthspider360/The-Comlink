from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="User_profile")
    avatar = CloudinaryField('profile', default="placeholder")
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

