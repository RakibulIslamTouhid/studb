# Generated by Django 2.0.2 on 2019-09-29 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='sec',
            new_name='section',
        ),
    ]
