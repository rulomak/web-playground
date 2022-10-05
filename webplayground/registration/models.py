from pickle import TRUE
from re import T
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename



class Profile(models.Model):                                       # models.OneToone   idica  solo puede existir un usuario para el mismo perfil   
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # on_ delete cascade  si se borra el usuario se borrara tambien todo en su perfil    
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Mete:
        ordering = ['user__username']
    """
    one to one field (1:1)  = 1 usuario - 1 perfil
    Foreign key field (1:N)  = 1 usuario <- N entradas
    many to many field (N:M)  = N entradas <-> M categorias 
    """
    
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print("se acaba de crear un usuario y su perfil enlazado")

