# Generated by Django 4.2 on 2024-06-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myporfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(default='No descripction'),
            preserve_default=False,
        ),
    ]
