"""App configuration for the encuesta app."""

from django.apps import AppConfig


class EncuestaConfig(AppConfig):
    """Encuesta app configuration."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "encuesta"
