# Generated by Django 2.2.1 on 2019-05-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_pizza_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='type',
            field=models.CharField(choices=[('RL', 'Regular'), ('SC', 'Sicilian')], max_length=20),
        ),
    ]
