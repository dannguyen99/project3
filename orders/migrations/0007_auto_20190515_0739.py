# Generated by Django 2.2.1 on 2019-05-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190515_0737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dinner_platter',
            old_name='price',
            new_name='price_small',
        ),
        migrations.RenameField(
            model_name='sub',
            old_name='price',
            new_name='price_small',
        ),
        migrations.RemoveField(
            model_name='dinner_platter',
            name='name',
        ),
        migrations.AddField(
            model_name='dinner_platter',
            name='price_large',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='sub',
            name='price_large',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
