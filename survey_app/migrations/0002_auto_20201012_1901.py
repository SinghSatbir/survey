# Generated by Django 3.0.7 on 2020-10-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='is_mandatory',
            new_name='mandatory',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(choices=[('Y', 'yes'), ('N', 'no')], max_length=1),
        ),
    ]
