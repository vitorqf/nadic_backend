# Generated by Django 4.2.1 on 2023-05-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
                ('plate', models.CharField(max_length=7)),
                ('chassis_type', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Cars',
            },
        ),
    ]