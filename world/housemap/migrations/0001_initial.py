# Generated by Django 2.1.5 on 2019-04-05 00:25

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', djgeojson.fields.PointField(default=dict)),
                ('description', models.TextField(default='')),
                ('picture', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ('-geom',),
            },
        ),
    ]