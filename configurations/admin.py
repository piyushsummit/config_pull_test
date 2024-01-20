from django.contrib import admin
from .models import Configuration, ProductType, Product, DisasterDeclaration

admin.site.register(Configuration)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(DisasterDeclaration)