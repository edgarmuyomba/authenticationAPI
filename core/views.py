from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def Index(request):
    return Response({"Success": "You have been successfully authenticated!"})