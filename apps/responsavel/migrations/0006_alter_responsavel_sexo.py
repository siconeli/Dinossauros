# Generated by Django 5.1.2 on 2024-10-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0005_responsavel_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsavel',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outros', 'Outros')], max_length=20),
        ),
    ]
