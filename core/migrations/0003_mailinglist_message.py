# Generated by Django 3.2 on 2022-08-09 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_client_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_of_start_mailing', models.DateTimeField()),
                ('text', models.TextField(max_length=1000)),
                ('filters', models.JSONField()),
                ('datetime_of_end_mailing', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Mailing List',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField()),
                ('client_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='core.mailinglist')),
                ('mailing_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mailing', to='core.mailinglist')),
            ],
        ),
    ]
