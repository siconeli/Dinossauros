# Generated by Django 5.1.2 on 2024-10-19 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_alter_aluno_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(default='teste', upload_to='fotos/'),
            preserve_default=False,
        ),
    ]
