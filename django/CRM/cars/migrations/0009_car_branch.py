# Generated by Django 4.2.1 on 2023-06-02 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
        ('cars', '0008_alter_car_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='branches.branch'),
        ),
    ]