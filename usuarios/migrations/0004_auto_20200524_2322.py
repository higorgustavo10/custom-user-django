# Generated by Django 3.0.6 on 2020-05-25 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20200524_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariocustom',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='usuariocustom',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Membro da Equipe'),
        ),
    ]
