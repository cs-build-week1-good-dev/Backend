# Generated by Django 2.2.3 on 2019-07-31 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='description',
        ),
        migrations.AddField(
            model_name='room',
            name='x_coordinate',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='room',
            name='y_coordinate',
            field=models.IntegerField(default=-1),
        ),
    ]
