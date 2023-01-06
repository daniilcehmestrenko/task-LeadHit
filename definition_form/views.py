from rest_framework.response import Response
from rest_framework.views import APIView

from .service import TemplateSearchEngine


class GetForm(APIView):

    def post(self, request):
        template = TemplateSearchEngine(request.data)
        
        return Response(template.data)
