# Generated by Django 3.2 on 2022-08-11 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_mailinglist_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='client_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='core.client'),
        ),
    ]