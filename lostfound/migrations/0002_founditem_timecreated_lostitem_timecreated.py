# Generated by Django 4.0 on 2021-12-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfound', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditem',
            name='timecreated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='lostitem',
            name='timecreated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
