from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import Profileform


def create_profile(request):
    if request.method == "POST":
        Profile_form = Profileform(request.POST, request.FILES)
        if Profile_form.is_valid():
            profile = Profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.add_message(request, messages.SUCCESS,
            'profile saved')
            return HttpResponseRedirect(reverse("profile")) #redirecting to a new URL
    Profile_form = Profileform()
    return render(request, "profile_page/profile_form.html", {"Profile_form": Profile_form})

@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    # profile_avatar = "1234"
    return render(request, "profile_page/profile.html",{'profile': profile})