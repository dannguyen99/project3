# Generated by Django 2.2.1 on 2019-06-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20190517_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='dinner_platter',
            name='carts',
            field=models.ManyToManyField(to='orders.Cart'),
        ),
        migrations.AddField(
            model_name='pasta',
            name='carts',
            field=models.ManyToManyField(to='orders.Cart'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='carts',
            field=models.ManyToManyField(to='orders.Cart'),
        ),
        migrations.AddField(
            model_name='salad',
            name='carts',
            field=models.ManyToManyField(to='orders.Cart'),
        ),
        migrations.AddField(
            model_name='sub',
            name='carts',
            field=models.ManyToManyField(to='orders.Cart'),
        ),
        migrations.AddField(
            model_name='topping',
            name='carts',
            field=models.ManyToManyField(to='orders.Cart'),
        ),
    ]