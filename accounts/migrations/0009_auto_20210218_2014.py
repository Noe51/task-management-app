# Generated by Django 3.1.6 on 2021-02-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210218_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='current_advancement',
            field=models.FloatField(default=0),
        ),
    ]
