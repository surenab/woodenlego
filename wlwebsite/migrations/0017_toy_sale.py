# Generated by Django 2.2.4 on 2019-08-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlwebsite', '0016_remove_toy_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='sale',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
