from django.conf import settings
from django.db import models


class Schema(models.Model):
    COL_SEP_CHOICES = [
        (",", "Comma (,)"),
        (";", "Semicolon (;)"),
        ("\t", "Tab (\t)"),
        (" ", "Space ( )"),
        ("|", "Vertical bar (|)"),
    ]

    QUOTE_CHOICES = [
        ('"', 'Double-quote (")'),
        ("'", "Single-quote (')"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_schemas"
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    column_separator = models.CharField(
        max_length=1,
        choices=COL_SEP_CHOICES,
        default=","
    )
    string_character = models.CharField(max_length=1, choices=QUOTE_CHOICES, default='"')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return f"/schemas/{self.pk}"

    def __str__(self):
        if self.title:
            return f"{self.title}"
        else:
            return "Untitled"


class SchemaColumn(models.Model):
    DATA_TYPES_CHOICES = [
        (0, "Full name (a combination of first name and last name)"),
        (1, "Job"),
        (2, "Email"),
        (3, "Domain name"),
        (4, "Phone number"),
        (5, "Company name"),
        (6, "Text (with specified range for a number of sentences)"),
        (7, "Integer (with specified range)"),
        (8, "Address"),
        (9, "Date"),
    ]

    target_schema = models.ForeignKey(
        Schema,
        on_delete=models.CASCADE,
        related_name="schema_columns"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="column name",
        blank=True, null=True
    )
    data_type = models.IntegerField(choices=DATA_TYPES_CHOICES, verbose_name="type")
    order = models.PositiveIntegerField(blank=True, default=0)
    data_range_from = models.PositiveIntegerField(blank=True, null=True, verbose_name="from")
    data_range_to = models.PositiveIntegerField(blank=True, null=True, verbose_name="to")
