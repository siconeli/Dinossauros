# Generated by Django 5.1.2 on 2024-10-30 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0006_alter_ficha_obs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='obs',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
