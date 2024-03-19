from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .forms import SignupForm
from .models import Profile

# Create your views here.
class Profile(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

    else:   
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})

def activate(request):
    return render(request, 'registration/active.html')
                                                                      