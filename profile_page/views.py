from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import Profileform
from feed.models import Post
from django.contrib.auth.models import User


def create_profile(request):
    
    if request.method == "POST":
        Profile_form = Profileform(request.POST, request.FILES)
        if Profile_form.is_valid():
            profile = Profile_form.save(commit=False)
            profile.user = request.user #associate the profile with logged in usr.
            profile.save()
            messages.add_message(request, messages.SUCCESS,
            'profile saved')
            return HttpResponseRedirect(reverse('users-profile')) # take back to profile after save.
    Profile_form = Profileform()
    return render(request, "profile_page/profile_form.html", {"Profile_form": Profile_form})

def edit_profile(request):
    """
    view to edit profile
    """
    profile = get_object_or_404(Profile, user =request.user) # get the logged in user.
    if request.method == "POST":
        profile_form = Profileform(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            # Profile = profile_form.save(commit=False)
            # Profile.save()
            profile_form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Updated!')
            return HttpResponseRedirect(reverse('users-profile'))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Profile!')
    else: 
        profile_form = Profileform(instance=profile) # pop form with current profile data.
    
    return render(request, "profile_page/profile_edit.html", {"profile_form": profile_form})

@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    user_posts = Post.objects.filter(author=request.user)
    
    context = {
        'profile': profile,
        'user_posts': user_posts
    }

    return render(request, "profile_page/profile.html", context)



   