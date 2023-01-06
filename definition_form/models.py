from django.db import models


class FieldForm(models.Model):
    FIELD_TYPE_CHOICES = (
                ('email', 'email'),
                ('phone', 'phone'),
                ('date', 'date'),
                ('text', 'text')
            )
    field_name = models.CharField(
                max_length=150,
                verbose_name='Название поля'
            )
    field_type = models.CharField(
                max_length=5,
                choices=FIELD_TYPE_CHOICES,
                verbose_name='Тип поля'
            )
    template_form = models.ForeignKey(
                'TemplateForm',
                on_delete=models.CASCADE,
                related_name='template_fields',
                verbose_name='Шаблон формы'
            )

    class Meta:
        ordering = ['template_form']


class TemplateForm(models.Model):
    template_name = models.CharField(
                max_length=150,
                verbose_name='Название шаблона'
            )

    def __str__(self):
        return self.template_name
