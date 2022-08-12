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
    status = models.BooleanField()
    mailing_id = models.OneToOneField(MailingList, on_delete=models.CASCADE, related_name='mailing')
    client_id = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return str(self.datetime)
