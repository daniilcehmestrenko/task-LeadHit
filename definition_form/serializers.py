from rest_framework import serializers

from .models import TemplateForm


class TemplateFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = TemplateForm
        fields = ('template_name',)
