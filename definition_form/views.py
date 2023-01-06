from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TemplateFormSerializer
from .service import TemplateSearchEngine


class GetForm(APIView):

    def post(self, request):
        validate_form = TemplateSearchEngine(request.data)
        template = validate_form.find_template()
        if template:
            serializer = TemplateFormSerializer(template, many=True)

            return Response(serializer.data)
        
        return Response(validate_form.data)
