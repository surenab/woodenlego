# Generated by Django 2.1.5 on 2019-07-10 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlwebsite', '0011_auto_20190710_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yerevan', models.IntegerField(blank=True, default=400, null=True)),
                ('county', models.IntegerField(blank=True, default=2000, null=True)),
            ],
        ),
    ]