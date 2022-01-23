# Generated by Django 4.0.1 on 2022-01-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('t', models.IntegerField()),
                ('v', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]