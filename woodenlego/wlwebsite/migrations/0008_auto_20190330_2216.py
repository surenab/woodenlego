# Generated by Django 2.1.5 on 2019-03-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlwebsite', '0007_toy_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='category',
            field=models.TextField(default='Toys', null=True),
        ),
    ]
