# Generated by Django 4.1.4 on 2022-12-13 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schema",
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
                ("name", models.CharField(max_length=100)),
                ("modified", models.DateTimeField(auto_now_add=True)),
                ("file", models.FileField(null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="DataSchemaRow",
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
                ("name", models.CharField(max_length=100)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("FULL_NAME", "Full name"),
                            ("JOB", "Job"),
                            ("EMAIL", "EMail"),
                            ("DOMAIN_NAME", "Domain name"),
                            ("PHONE_NUMBER", "Phone number"),
                            ("COMPANY_NAME", "Company name"),
                            ("TEXT", "Text"),
                            ("INTEGER", "Integer"),
                            ("ADDRESS", "Address"),
                            ("DATE", "Date"),
                        ],
                        default="FULL_NAME",
                        max_length=12,
                    ),
                ),
                ("start_range", models.PositiveIntegerField()),
                ("stop_range", models.PositiveIntegerField()),
                ("order_queue", models.PositiveIntegerField()),
                (
                    "schema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.schema"
                    ),
                ),
            ],
        ),
    ]
