# Generated by Django 2.0.5 on 2018-05-28 21:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 28, 21, 6, 17, 40168, tzinfo=utc), verbose_name='Fecha de Publicación'),
        ),
    ]
