# Generated by Django 4.0.6 on 2022-11-17 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='itemName',
            field=models.TextField(),
        ),
    ]
