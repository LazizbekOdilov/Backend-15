# Generated by Django 4.2.5 on 2023-10-04 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('akkaunt', '0007_alter_xodim_oylik_foydalanuvchi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foydalanuvchi',
            name='talaba',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='akkaunt.talaba'),
        ),
    ]
