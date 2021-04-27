# Generated by Django 3.2 on 2021-04-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_painting_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='remark',
            field=models.TextField(blank=True, help_text="Enter any remark that doesn't match any other category", max_length=200, null=True),
        ),
    ]
