# Generated by Django 2.2.6 on 2019-11-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20191115_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
