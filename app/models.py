import uuid
import pytz
from django.db import models
from django.utils import timezone


# Create your models here.
class ActivityPeriod(models.Model):

    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)

    class Meta:
        verbose_name_plural = "ActivityPeriods"


class User(models.Model):

    # timezone
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    real_name = models.CharField(max_length=225)
    tz = models.CharField(max_length=32, choices=TIMEZONES)
    activity_periods = models.ManyToManyField(ActivityPeriod)

    class Meta:
        verbose_name_plural = "Users"
