# Generated by Django 2.1.5 on 2019-03-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlwebsite', '0004_auto_20190328_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='mainimage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
