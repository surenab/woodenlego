# Generated by Django 2.1.5 on 2019-07-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190710_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='delivery_date',
            field=models.DateField(null=True),
        ),
    ]