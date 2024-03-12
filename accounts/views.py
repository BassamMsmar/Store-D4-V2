from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Profile

# Create your views here.
class Profile(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

def register(request):
    return render(request, 'registration/register.html')

