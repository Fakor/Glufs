# Generated by Django 2.2.7 on 2019-12-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='recipe',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='notes',
            field=models.ManyToManyField(to='main.Note'),
        ),
    ]