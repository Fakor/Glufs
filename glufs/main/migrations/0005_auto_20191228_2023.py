# Generated by Django 2.2.7 on 2019-12-28 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191227_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='classification',
        ),
        migrations.DeleteModel(
            name='Classification',
        ),
    ]
