from django.db.models.signals import post_save
#from django.contrib.auth.models import User
from django.dispatch import receiver
from staff.models import User
from .models import Profile, Staff


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_staff(sender, instance, created, **kwargs):
    if created:
        Staff.objects.create(staff=instance)


@receiver(post_save, sender=User)
def save_staff(sender, instance, **kwargs):
    instance.staff.save()
