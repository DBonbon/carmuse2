# Generated by Django 3.2 on 2021-04-26 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_painting_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='catalog.category'),
        ),
        migrations.AlterField(
            model_name='painting',
            name='medium',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.medium'),
        ),
        migrations.AlterField(
            model_name='painting',
            name='support',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.support'),
        ),
    ]
