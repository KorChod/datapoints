# Generated by Django 4.0.1 on 2022-01-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='v',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
