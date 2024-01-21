# serializers.py
from rest_framework import serializers
from .models import Configuration, Product, DisasterDeclaration, Loan

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DisasterDeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterDeclaration
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'