from django.db import models
from django.utils import timezone


class Subscriptor(models.Model):
    client = models.CharField(
        max_length=100,
    )
    account = models.CharField(
        max_length=100,
    )
    date_created = models.DateTimeField(
        default=timezone.now,
    )
    coupon_used = models.CharField(
        max_length=100,
    )

    def __unicode__(self):
        return ":".join([self.title, str(self.username)])

    class Meta:
        db_table = "subscriptor"
        index_together = [["client", "account"]]
        unique_together = ("client", "account")
