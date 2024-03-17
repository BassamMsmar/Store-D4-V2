from django.urls import path

from .views import Profile , register

urlpatterns = [
     path('profile/<int:pk>', Profile.as_view() , name='profile'),
     path('register', register, name='register'),
     
]