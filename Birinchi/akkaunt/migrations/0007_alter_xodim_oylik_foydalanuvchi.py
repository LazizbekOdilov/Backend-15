# Generated by Django 4.2.5 on 2023-10-04 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('akkaunt', '0006_talaba_xodim_alter_kontakt_jins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xodim',
            name='oylik',
            field=models.PositiveIntegerField(verbose_name='Oylik maosh ... $ da '),
        ),
        migrations.CreateModel(
            name='Foydalanuvchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akkaunt.talaba')),
            ],
        ),
    ]
