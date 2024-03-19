from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView


from .forms import SignupForm
from .models import Profile
from .form import SignUpForm, ActivateForm

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
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save(commit=False)
            user.is_active = False

            form.save()
            profile = Profile.objects.get(user__username=username)

            from django.core.mail import send_mail

            send_mail(
                "Activate Your Account",
                f"Welcome {username} \nUse this code {profile.code} to activate your account",
                "from@example.com",
                [email],
                fail_silently=False,
            )
            
            return redirect(f'/accounts/{username}/activate')


            
    else:
        form = SignUpForm()
    
    return render(request, 'registration/register.html', {'form':form})


def activate(request, username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
         form = ActivateForm(request.POST)
         if form.is_valid():
             code = form.cleaned_data['code']
             if code == profile.code:
                profile.user.is_active = True
                profile.code = ''
                profile.user.save()

                return redirect('/accounts/login')
    else:
        form = ActivateForm()


             
    return render(request, 'accounts/activate.html', {'form':form})
