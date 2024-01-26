from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Configuration, Product, DisasterDeclaration, Loan, FlutterLoan
from .serializers import ConfigurationSerializer, ProductSerializer, DisasterDeclarationSerializer, LoanSerializer, FlutterLoanSerializer
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
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    configurations = Product.objects.all()
    serializer = ProductSerializer(configurations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_disaster_declarations(request):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    configurations = DisasterDeclaration.objects.all()
    serializer = DisasterDeclarationSerializer(configurations, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def get_post_loans(request):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
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

@api_view(['GET', 'POST'])
def get_post_flutter_loans(request):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    if request.method == 'GET':
        flutter_loans = FlutterLoan.objects.all()
        serializer = FlutterLoanSerializer(flutter_loans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlutterLoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)