# Generated by Django 2.1.8 on 2019-05-23 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='club_image',
            new_name='event_image',
        ),
    ]