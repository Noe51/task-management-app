# Generated by Django 3.1.6 on 2021-02-04 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210203_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='client_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.client'),
        ),
    ]
