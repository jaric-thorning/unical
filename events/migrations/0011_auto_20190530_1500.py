# Generated by Django 2.1.8 on 2019-05-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20190530_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, default=False, help_text='Description', verbose_name='Description'),
        ),
    ]
