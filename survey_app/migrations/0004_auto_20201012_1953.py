# Generated by Django 3.0.7 on 2020-10-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0003_auto_20201012_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='update_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='survey',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
    ]
