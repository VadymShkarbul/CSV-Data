from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic
from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from app.forms import SchemaForm, SchemaColumnInline
# from django.shortcuts import redirect, render

# from app.forms import DataSchemaForm, SchemaFormSet
from app.models import Schema


class SchemaListView(LoginRequiredMixin, generic.ListView):
    model = Schema
    template_name = "schema_list.html"

    def get_queryset(self):
        queryset = Schema.objects.filter(user=self.request.user)
        return queryset


class SchemaUpdateView(LoginRequiredMixin, UpdateWithInlinesView):
    model = Schema
    form_class = SchemaForm
    inlines = [
        SchemaColumnInline,
    ]
    template_name = "schema_form.html"

    # success_url = reverse_lazy("schemas")

    def get_initial(self):
        data = {"user": self.request.user}
        return data

    def get_success_url(self):
        if "action" in self.request.POST:
            if self.request.POST["action"] == "submit":
                return reverse("schemas")
            if self.request.POST["action"] == "add_column":
                obj = self.object
                return reverse("schema_update", kwargs={"pk": obj.pk})

        else:
            return reverse("schemas")


class SchemaCreateView(LoginRequiredMixin, CreateWithInlinesView):
    model = Schema
    form_class = SchemaForm
    inlines = [
        SchemaColumnInline,
    ]
    template_name = "schema_form.html"

    # success_url = reverse_lazy("schemas")

    def get_initial(self):
        data = {"user": self.request.user}
        return data

    def get_success_url(self):
        if "action" in self.request.POST:
            if self.request.POST["action"] == "submit":
                return reverse("schemas")
            if self.request.POST["action"] == "add_column":
                obj = self.object
                return reverse("schema_update", kwargs={"pk": obj.pk})

        else:
            return reverse("schemas")


class SchemaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Schema
    template_name = "schema_confirm_delete.html"
    success_url = reverse_lazy("schemas")
