# Generated by Django 5.1.2 on 2024-10-19 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0004_responsavel_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsavel',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], default='Feminino', max_length=20),
            preserve_default=False,
        ),
    ]
