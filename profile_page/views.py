from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'profile_page/profile.html')
    
