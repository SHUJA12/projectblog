# Generated by Django 2.2.2 on 2020-12-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_auto_20201223_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_time',
        ),
        migrations.AddField(
            model_name='comment',
            name='time_added',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
