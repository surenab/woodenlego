# Generated by Django 2.1.5 on 2019-03-27 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlwebsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='image1',
            field=models.ImageField(upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image2',
            field=models.ImageField(upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image3',
            field=models.ImageField(upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='image4',
            field=models.ImageField(upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='mainimage',
            field=models.ImageField(upload_to='static/image'),
        ),
    ]
