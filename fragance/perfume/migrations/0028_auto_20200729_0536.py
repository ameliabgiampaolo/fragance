# Generated by Django 3.0.8 on 2020-07-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume', '0027_auto_20200729_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vam_ingrediente_esencia',
            name='fecha_caducidad',
            field=models.DateField(null=True),
        ),
    ]
