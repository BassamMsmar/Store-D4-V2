from django.urls import path

from .views import ProfileDetailView , register, activate


urlpatterns = [
     path('profile/<int:pk>', ProfileDetailView.as_view() , name='profile'),
     path('register', register, name='register'),
     path('<str:username>/activate', activate, name='activate'),
     
]