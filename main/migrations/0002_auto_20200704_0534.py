# Generated by Django 3.0.8 on 2020-07-04 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='textarea',
            new_name='message',
        ),
    ]
