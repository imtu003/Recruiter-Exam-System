# Generated by Django 2.2.6 on 2019-12-17 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20191217_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedchoices',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selected_choice', to='exam.Question'),
        ),
    ]
