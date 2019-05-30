# Generated by Django 2.1.8 on 2019-05-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20190525_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='followed',
            field=models.BooleanField(blank=True, help_text='Followed', null=True, verbose_name='Followed'),
        ),
        migrations.AlterField(
            model_name='club',
            name='fb',
            field=models.CharField(blank=True, help_text='Page Link - https://www.facebook.com/#####', max_length=100, verbose_name='Facebook Page'),
        ),
        migrations.AlterField(
            model_name='club',
            name='instagram',
            field=models.CharField(blank=True, help_text='Instagram Link - https://www.instagram.com/#####', max_length=100, verbose_name='Instagram Page'),
        ),
    ]
