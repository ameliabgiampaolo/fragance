# Generated by Django 3.0.8 on 2020-07-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume', '0020_auto_20200729_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vam_condicion_envio',
            name='costo',
            field=models.IntegerField(),
        ),
    ]
