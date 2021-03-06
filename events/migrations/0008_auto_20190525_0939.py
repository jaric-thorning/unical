# Generated by Django 2.1.8 on 2019-05-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20190525_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='website',
        ),
        migrations.AddField(
            model_name='club',
            name='email',
            field=models.CharField(blank=True, help_text='Email Link', max_length=100, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='club',
            name='instagram',
            field=models.CharField(blank=True, help_text='Instagram Link', max_length=100, verbose_name='Instagram Page'),
        ),
        migrations.AddField(
            model_name='club',
            name='web',
            field=models.CharField(blank=True, help_text='Website Link', max_length=100, verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='club',
            name='fb',
            field=models.CharField(blank=True, help_text='Page Link', max_length=100, verbose_name='Facebook Page'),
        ),
        migrations.AlterField(
            model_name='club',
            name='location',
            field=models.CharField(blank=True, help_text='Club Location', max_length=100, verbose_name='Location'),
        ),
    ]
