# Generated by Django 2.2.2 on 2019-12-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_auto_20191216_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_bus',
            name='arrivaltime',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='add_bus',
            name='bus_no',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='add_bus',
            name='departuretime',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
