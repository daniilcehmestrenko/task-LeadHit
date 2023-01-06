from django.db.models import Q
from .validators import ValidateDate, ValidateEmail, ValidatePhone
from .models import TemplateForm


class TemplateSearchEngine:
    TYPE_FIELD = {
            'email': ValidateEmail(),    
            'date': ValidateDate(),
            'phone': ValidatePhone()
        }

    def __init__(self, data):
        self.data = self.__validated_data(data)

    def __type_definition(self, value: str):
        for type_field, validator in self.TYPE_FIELD.items():
            if validator(value): 
                
                return type_field

        return 'text'
            

    def __validated_data(self, data: dict):
        for key, value in data.items():
            data[key] = self.__type_definition(value)

        return data

    def find_template(self):
        template = TemplateForm.objects.all()

        for name_field, type_field in self.data.items():
            query = Q(template_fields__field_name=name_field) & \
                    Q(template_fields__field_type=type_field)
            template = template.filter(query)

        if template:
            return template

        return None
