# Generated by Django 4.2.5 on 2023-10-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akkaunt', '0004_alter_kontakt_sana'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontakt',
            name='jins',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
