from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Configuration
from .serializers import ConfigurationSerializer

@api_view(['GET'])
def get_configurations(request):
    configurations = Configuration.objects.all()
    serializer = ConfigurationSerializer(configurations, many=True)
    return Response(serializer.data)
