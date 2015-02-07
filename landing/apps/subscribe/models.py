from django.db import models
from django.utils import timezone


class Subscriptor(models.Model):
    client = models.BigIntegerField()
    account = models.BigIntegerField()
    date_created = models.DateTimeField(
        default=timezone.now,
    )
    lifetime = models.PositiveSmallIntegerField(
        default=3,
    )
    is_active = models.BooleanField(
        default=True,
    )

    def __unicode__(self):
        return ":".join([str(self.client), str(self.account)])

    class Meta:
        db_table = "subscriptor"
        index_together = [["client", "account"]]
        unique_together = ("client", "account")


from .signals import update_subscriptor
