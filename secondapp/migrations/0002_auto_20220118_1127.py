# Generated by Django 2.2.5 on 2022-01-18 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Curriculum',
            new_name='Course',
        ),
    ]
