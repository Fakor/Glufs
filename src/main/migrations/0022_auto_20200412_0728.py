# Generated by Django 3.0.2 on 2020-04-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200412_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]