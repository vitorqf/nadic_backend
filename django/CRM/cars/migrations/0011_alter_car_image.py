# Generated by Django 4.2.1 on 2023-07-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.FileField(null=True, upload_to='cars'),
        ),
    ]
