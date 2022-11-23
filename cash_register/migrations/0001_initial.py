# Generated by Django 4.0.6 on 2022-11-17 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCode', models.CharField(max_length=10)),
                ('itemName', models.CharField(max_length=50)),
                ('itemPrice', models.FloatField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
    ]
