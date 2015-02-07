from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subscriptor


@receiver(post_save, sender=Subscriptor)
def update_subscriptor(sender, instance=None, created=False, **kwargs):
    post_save.disconnect(update_subscriptor, sender=Subscriptor)
    subscriptor = instance
    if subscriptor.lifetime == 0:
        subscriptor.is_active = False
        subscriptor.save()
    post_save.connect(update_subscriptor, sender=Subscriptor)
