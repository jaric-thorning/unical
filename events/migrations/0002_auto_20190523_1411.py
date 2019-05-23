# Generated by Django 2.1.8 on 2019-05-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='notes',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, help_text='Description', null=True, verbose_name='Description'),
        ),
    ]
