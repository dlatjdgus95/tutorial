# Generated by Django 2.2.5 on 2022-01-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0003_army_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armyshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
                ('type', models.TextField()),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'army_shop',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Army_shop',
        ),
    ]
