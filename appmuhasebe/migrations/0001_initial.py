# Generated by Django 4.2.11 on 2025-04-09 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OnayDefterKayitModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("olurNo", models.CharField(max_length=4)),
                (
                    "olurAciklama",
                    models.CharField(default="my_default_value", max_length=110),
                ),
                ("olurTarih", models.DateField()),
                ("olurOdemeTutar", models.CharField(max_length=20)),
                ("olurParaBirimi", models.CharField(max_length=20)),
                ("olurOdemeYolu", models.CharField(max_length=20)),
                (
                    "username",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
