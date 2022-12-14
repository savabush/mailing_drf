# Generated by Django 3.2 on 2022-08-14 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_mailinglist_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='code_of_mobile_operator',
            field=models.CharField(editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="The client's phone number in the format 7XXXXXXXXXX (X - number from 0 to 9)", regex='7\\d{10}')]),
        ),
    ]
