# Generated by Django 2.2.6 on 2019-12-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20191210_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionchoice',
            name='is_right_answer',
        ),
        migrations.AddField(
            model_name='choice',
            name='is_right_choice',
            field=models.BooleanField(default=False),
        ),
    ]
