# Generated by Django 3.0.8 on 2020-07-29 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfume', '0009_auto_20200729_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vam_miembro_ifra',
            name='id_productor',
            field=models.ForeignKey(db_column='id_productor', null=True, on_delete=django.db.models.deletion.CASCADE, to='perfume.vam_productor'),
        ),
    ]
