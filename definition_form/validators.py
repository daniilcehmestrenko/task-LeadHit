import re
from django.core.validators import validate_email


class ValidateEmail:

    def __call__(self, value: str):
        try:
            validate_email(value)
            
            return True
        except:
            
            return False


class ValidatePhone:

    def __call__(self, value: str):
        
        if re.fullmatch(r'\+7\d{10}', value):
            
            return True
        
        return False


class ValidateDate:

    def __call__(self, value: str):

        if re.fullmatch(r'\d\d.\d\d.\d{4}', value) or \
           re.fullmatch(r'\d{4}-\d\d-\d\d', value):
            
            return True

        return False
