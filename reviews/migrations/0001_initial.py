# Generated by Django 4.1.2 on 2022-11-17 15:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                (
                    "stars",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                ("review", models.TextField()),
                ("spoilers", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "recomendation",
                    models.CharField(
                        choices=[
                            ("Avoid Watch", "Avoid Watch"),
                            ("Should Watch", "Should Watch"),
                            ("Must Watch", "Must Watch"),
                            ("No Opinion", "No Opinion"),
                        ],
                        default="No Opinion",
                        max_length=50,
                    ),
                ),
                (
                    "critic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="movies.movie",
                    ),
                ),
            ],
        ),
    ]
