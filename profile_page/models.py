from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    rank = models.CharField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    avatar = CloudinaryField('Avatar', default="clone.placeholder.webp")
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username

