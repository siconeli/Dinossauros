# Generated by Django 5.1.2 on 2024-10-19 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_aluno_foto'),
        ('ficha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno'),
            preserve_default=False,
        ),
    ]