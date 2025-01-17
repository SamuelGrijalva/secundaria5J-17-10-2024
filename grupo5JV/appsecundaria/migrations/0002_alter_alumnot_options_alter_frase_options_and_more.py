# Generated by Django 5.1.1 on 2024-10-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsecundaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnot',
            options={'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
        migrations.AlterModelOptions(
            name='frase',
            options={'verbose_name': 'Frase', 'verbose_name_plural': 'frases'},
        ),
        migrations.AlterField(
            model_name='alumnot',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre (s)'),
        ),
        migrations.AlterModelTable(
            name='alumnot',
            table='Alumnos',
        ),
    ]
