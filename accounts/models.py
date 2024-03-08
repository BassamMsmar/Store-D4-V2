from django.db import models
from django.contrib.auth.models import User

from utils.generate_code import generate_code

Permissions = (
    ('Admin','Admin'),
    ('User','User'),
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    code = models.CharField(max_length=9, default=generate_code())
    phone = models.CharField(max_length=16, null=True, blank=True)
    permission = models.CharField(max_length=5, choices=Permissions, default='User')



    def __str__(self):
        return self.user.username