# Generated by Django 5.1.2 on 2024-10-24 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0004_alter_ficha_alergico_alter_ficha_convulsoes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='obs',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]
