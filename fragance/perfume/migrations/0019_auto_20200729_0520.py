# Generated by Django 3.0.8 on 2020-07-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume', '0018_auto_20200729_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vam_condicion_pago',
            name='porcen_cuota',
            field=models.IntegerField(null=True),
        ),
    ]
