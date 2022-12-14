from django.core.validators import RegexValidator
from django.db import models


class Client(models.Model):
    phone_regex = RegexValidator(
        regex=r'7\d{10}',
        message="The client's phone number in the format 7XXXXXXXXXX (X - number from 0 to 9)"
    )
    phone = models.CharField(max_length=11, unique=True, validators=[phone_regex])
    code_of_mobile_operator = models.CharField(max_length=3, editable=False)
    tag = models.CharField(max_length=10)

    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    timezone = models.CharField(choices=TIMEZONES, max_length=100)

    def __str__(self):
        return self.phone

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.code_of_mobile_operator = str(self.phone)[1:4]
        return super().save(force_insert, force_update, using, update_fields)


class MailingList(models.Model):
    datetime_of_start_mailing = models.DateTimeField()
    text = models.TextField(max_length=1000)
    filters = models.JSONField()
    datetime_of_end_mailing = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Mailing List'

    def __str__(self):
        return str(self.datetime_of_end_mailing)


class Message(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    mailing = models.ForeignKey(MailingList, on_delete=models.CASCADE, related_name='mailing')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return str(self.datetime)
