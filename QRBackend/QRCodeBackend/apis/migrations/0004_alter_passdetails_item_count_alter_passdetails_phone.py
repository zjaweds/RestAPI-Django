# Generated by Django 4.0.4 on 2022-05-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_passdetails_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passdetails',
            name='item_count',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='passdetails',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]