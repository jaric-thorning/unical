# Generated by Django 2.1.8 on 2019-05-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20190530_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='followed',
        ),
        migrations.AddField(
            model_name='club',
            name='followed',
            field=models.BooleanField(blank=True, help_text='Followed', null=True, verbose_name='Followed'),
        ),
    ]
