from django.urls import path

from .views import ProfileDetailView , register

urlpatterns = [
     path('profile/<int:pk>', ProfileDetailView.as_view() , name='profile'),
     path('register', register, name='register'),
     
]