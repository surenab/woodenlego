# Generated by Django 2.1.5 on 2019-03-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlwebsite', '0002_auto_20190327_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='manufactor',
            field=models.TextField(blank=True, default='WoodenLego', null=True),
        ),
    ]