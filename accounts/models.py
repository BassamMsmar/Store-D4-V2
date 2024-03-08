from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.generate_code import generate_code

Permissions = (
    ('Admin','Admin'),
    ('User','User'),
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile_user', on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile')
    code = models.CharField(max_length=9, default=generate_code())
    permission = models.CharField(max_length=5, choices=Permissions, default='User')



    def __str__(self):
        return self.user.username
    
TYPE_PHONE = (
    ('Primary', 'primary'),
    ('Secondary', 'secondary'),
    ('Tertiary', 'tertiary'),
    
)
class Phone(models.Model):
    user = models.ForeignKey(User, related_name='phone_user', on_delete=models.CASCADE)
    phone = models.CharField(max_length=16)
    type = models.CharField(max_length=9, choices=TYPE_PHONE, default='Primary')


ADDRESS_TYPE = (
    ('Home', 'Home'),
    ('Office', 'Office'),
    ('Bussiness', 'Bussiness'),
)

class Address(models.Model):
    user = models.ForeignKey(User, related_name='address_user', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=9, choices=ADDRESS_TYPE, default='home')
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)