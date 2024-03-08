from django.urls import path

from .views import Profile 

urlpatterns = [
     path('profile/<int:pk>', Profile.as_view() , name='profile'),
]