# Generated by Django 3.0.8 on 2020-07-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume', '0031_auto_20200729_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vam_ingrediente_otro',
            name='ipc_numeric',
            field=models.IntegerField(null=True),
        ),
    ]
