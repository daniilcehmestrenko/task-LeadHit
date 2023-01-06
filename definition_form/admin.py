from django.contrib import admin

from .models import FieldForm, TemplateForm


class FieldFormInLine(admin.StackedInline):
    model = FieldForm
    extra = 1


@admin.register(TemplateForm)
class TemplateFormAdmin(admin.ModelAdmin):
    list_display = ('template_name',)
    inlines = (FieldFormInLine,)

