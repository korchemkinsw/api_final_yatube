# Generated by Django 3.2.3 on 2021-06-02 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210531_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
    ]
