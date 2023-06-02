# Generated by Django 4.2.1 on 2023-06-02 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.CharField(choices=[(1, 'Available'), (2, 'Unavailable')], default=1, max_length=20, null=True),
        ),
    ]