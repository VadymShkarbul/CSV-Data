from django import forms
from extra_views import InlineFormSetFactory

from app.models import Schema, SchemaColumn


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = "__all__"
        # exclude = ("user",)
        widgets = {
            "user": forms.HiddenInput(),
            "title": forms.TextInput(),
            "column_separator": forms.Select(),
            "string_character": forms.Select(),
        }


class SchemaColumnForm(forms.ModelForm):
    class Meta:
        model = SchemaColumn
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(),
            "order": forms.NumberInput(),
            "data_type": forms.Select(),
            "data_range_from": forms.NumberInput(),
            "data_range_to": forms.NumberInput(),
        }


class SchemaColumnInline(InlineFormSetFactory):
    model = SchemaColumn
    form_class = SchemaColumnForm
    fields = "__all__"

    # exclude = ("target_schema",)
    factory_kwargs = {
        "extra": 1,
        "max_num": None,
        "can_order": True,
        "can_delete": True,
    }
