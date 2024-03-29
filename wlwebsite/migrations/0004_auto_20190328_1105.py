# Generated by Django 2.1.5 on 2019-03-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlwebsite', '0003_auto_20190327_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='price',
            field=models.IntegerField(blank=True, default=1000, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='real_price',
            field=models.IntegerField(blank=True, default=1000, null=True),
        ),
    ]
