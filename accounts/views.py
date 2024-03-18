from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Profile
from .form import SignUpForm

# Create your views here.
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    def get_object(self, queryset=None):
            # Assuming 'pk' is the primary key of the associated User instance
            user_pk = self.kwargs.get('pk')
            object = Profile.objects.get(user_id=user_pk)
            return object




def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/register_done.html')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/register.html', {'form':form})


def activate(request):
    return render(request, 'registration/activate.html')
