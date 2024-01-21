from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Configuration, Product, DisasterDeclaration, Loan
from .serializers import ConfigurationSerializer, ProductSerializer, DisasterDeclarationSerializer, LoanSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import permissions
from rest_framework import status



@api_view(['GET'])
def get_configurations(request):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
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

@api_view(['GET', 'POST'])
def get_post_loans(request):
    if request.method == 'GET':
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)