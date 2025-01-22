from django.urls import path
from .views import profile, create_profile

urlpatterns = [
    path('', profile, name='users-profile'),
    path('createprofile/', create_profile, name='createprofile'),
]