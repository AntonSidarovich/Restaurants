# Generated by Django 3.0.3 on 2021-07-15 08:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 7, 15, 8, 59, 55, 95080, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='describtion',
            field=models.TextField(),
        ),
    ]