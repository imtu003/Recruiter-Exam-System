# Generated by Django 2.2.6 on 2019-12-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_exam_queston'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]