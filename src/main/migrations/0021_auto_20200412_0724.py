# Generated by Django 3.0.2 on 2020-04-12 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200411_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='text',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
