from django.contrib import admin
from .models import Configuration, ProductType, Product, DisasterDeclaration, Loan, FlutterLoan

admin.site.register(Configuration)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(DisasterDeclaration)
admin.site.register(Loan)
admin.site.register(FlutterLoan)