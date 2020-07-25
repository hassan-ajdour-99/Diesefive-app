# Generated by Django 3.0.3 on 2020-03-02 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='update_date',
        ),
        migrations.AddField(
            model_name='posts',
            name='post_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
