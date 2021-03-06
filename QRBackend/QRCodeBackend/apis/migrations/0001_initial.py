# Generated by Django 4.0.4 on 2022-05-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=40)),
                ('pass_type', models.CharField(max_length=20)),
                ('item_count', models.IntegerField()),
                ('full_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('payment_Id', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
