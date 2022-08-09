from django.db import models


class Client(models.Model):
    phone = models.CharField(max_length=11, unique=True)
    code_of_mobile_operator = models.CharField(max_length=3)
    tag = models.CharField(max_length=10)

    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    timezone = models.CharField(choices=TIMEZONES, max_length=100)

    def __str__(self):
        return self.phone
