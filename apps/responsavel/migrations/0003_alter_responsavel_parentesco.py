# Generated by Django 5.1.1 on 2024-10-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0002_rename_aluno_resp_responsavel_aluno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsavel',
            name='parentesco',
            field=models.CharField(choices=[('Pais', 'Pais'), ('Avós', 'Avós'), ('Tios', 'Tios'), ('Primos', 'Primos'), ('Outros', 'Outros')], max_length=20),
        ),
    ]
