# Generated by Django 2.2.7 on 2020-01-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191229_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='labels',
            field=models.ManyToManyField(to='main.Label'),
        ),
    ]