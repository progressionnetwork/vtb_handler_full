from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProcessingFile, User


@receiver(post_save, sender=ProcessingFile)
def post_save_raw_file(sender, instance, created, **kwargs):
    if created:
        pass


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(pk = instance.pk)
        user.is_active = False
        user.save()
