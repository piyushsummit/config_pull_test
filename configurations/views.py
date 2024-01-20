from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Configuration, Product, DisasterDeclaration
from .serializers import ConfigurationSerializer, ProductSerializer, DisasterDeclarationSerializer

@api_view(['GET'])
def get_configurations(request):
    configurations = Configuration.objects.all()
    serializer = ConfigurationSerializer(configurations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_products(request):
    configurations = Product.objects.all()
    serializer = ProductSerializer(configurations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_disaster_declarations(request):
    configurations = DisasterDeclaration.objects.all()
    serializer = DisasterDeclarationSerializer(configurations, many=True)
    return Response(serializer.data)