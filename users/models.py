from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email =models.EmailField(blank=True,null=True)
    photo =models.ImageField(blank=True,null=True)
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.user.username)
    
#def create_user_profile(sender, instance, created, **kwargs):
    #if created:
        #Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
    #if created:
        #Profile.objects.create(user=instance)