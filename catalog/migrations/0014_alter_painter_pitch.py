# Generated by Django 3.2.3 on 2021-05-17 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_painter_pitch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painter',
            name='pitch',
            field=models.TextField(blank=True, help_text="Pitch pour capter l'attention", max_length=500, null=True),
        ),
    ]