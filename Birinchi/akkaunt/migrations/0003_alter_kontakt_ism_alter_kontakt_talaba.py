# Generated by Django 4.2.5 on 2023-10-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akkaunt', '0002_universitet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontakt',
            name='ism',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='kontakt',
            name='talaba',
            field=models.BooleanField(default=True),
        ),
    ]
