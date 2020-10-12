# Generated by Django 3.0.7 on 2020-10-12 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0002_auto_20201012_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='update_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='survey',
            name='added_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='survey',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]