# Generated by Django 5.1.2 on 2024-10-19 04:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('cuidado_especial', models.BooleanField(default=False)),
                ('alergico', models.BooleanField(default=False)),
                ('intolerante', models.BooleanField(default=False)),
                ('quedas', models.BooleanField(default=False)),
                ('refluxo', models.BooleanField(default=False)),
                ('convulsoes', models.BooleanField(default=False)),
                ('remedio_continuo', models.BooleanField(default=False)),
                ('obs', models.TextField(default=False)),
                ('usuario_criador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
