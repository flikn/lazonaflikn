from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyUser


@receiver(post_save, sender=MyUser)
def update_user(sender, instance=None, created=False, **kwargs):
    post_save.disconnect(update_user, sender=MyUser)
    user = instance
    if user.subscriptor:
        user.was_registered = True
        user.save()
    post_save.connect(update_user, sender=MyUser)
