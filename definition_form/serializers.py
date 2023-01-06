from rest_framework import serializers

from .models import TemplateForm


class TemplateFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateForm
        fields = ('template_name',)
