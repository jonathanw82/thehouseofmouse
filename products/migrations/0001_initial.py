# Generated by Django 2.2.6 on 2019-10-11 12:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('gift_wrap', models.BooleanField(default=True)),
                ('tags', models.CharField(max_length=300)),
                ('num_in_stock', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('num_sold', models.PositiveSmallIntegerField(default=0)),
                ('num_fav', models.PositiveSmallIntegerField(default=0)),
                ('shipping_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.Shipping_profile')),
            ],
        ),
    ]
