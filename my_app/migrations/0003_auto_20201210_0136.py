# Generated by Django 3.1.4 on 2020-12-09 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20201210_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='time',
            new_name='oreder_number',
        ),
    ]