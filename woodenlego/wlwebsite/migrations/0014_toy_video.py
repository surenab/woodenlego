# Generated by Django 2.1.5 on 2019-07-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlwebsite', '0013_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='static/image'),
        ),
    ]
