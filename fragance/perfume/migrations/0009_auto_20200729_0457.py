# Generated by Django 3.0.8 on 2020-07-29 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume', '0008_auto_20200729_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vam_escala_valorada',
            name='fecha_final',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='vam_escala_valorada',
            name='rango_fin',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vam_miembro_ifra',
            name='fecha_final',
            field=models.DateField(null=True),
        ),
    ]
