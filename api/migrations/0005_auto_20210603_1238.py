# Generated by Django 3.2.3 on 2021-06-03 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_rename_author_follow_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(help_text='интересный автор', on_delete=django.db.models.deletion.CASCADE, related_name='following', to='auth.user', verbose_name='интересный автор'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(help_text='подписчик', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='auth.user', verbose_name='подписчик'),
        ),
    ]