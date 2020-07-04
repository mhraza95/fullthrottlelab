import random
from django.core.management.base import BaseCommand
from app.models import User, ActivityPeriod
import random
import time
import pytz


def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d %H:%M:%S', prop)


class Command(BaseCommand):
    """
    https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/
    https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    This command is for inserting ActivityPeriod, User into database.
    Insert 5 User, 5 Activity.
    """

    def handle(self, *args, **options):

        # create 5 activity periods
        activity_period = [ActivityPeriod(start_time=random_date("2009-01-01 1:30:00", "2010-01-01 4:50:00", random.random()),
                                     end_time=random_date("2009-01-01 1:30:00", "2010-01-01 4:50:00", random.random()))
                            for _ in range(5)]

        ActivityPeriod.objects.bulk_create(activity_period)

        # create 5 users into Db
        TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
        for i in range(5):

            user = User.objects.create(real_name=f"name{i+1}", tz=TIMEZONES[random.randint(0, len(TIMEZONES))][0])
            user.activity_periods.set(ActivityPeriod.objects.all()[i:i+1])
            user.save()

        print("Added {} Users into DB".format(i+1))
