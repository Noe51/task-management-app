# Generated by Django 3.1.6 on 2021-02-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210218_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='current_advancement',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]