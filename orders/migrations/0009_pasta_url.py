# Generated by Django 2.2.1 on 2019-05-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190515_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasta',
            name='url',
            field=models.CharField(default='/static/orders/images/pasta-1.jpg', max_length=1000),
        ),
    ]