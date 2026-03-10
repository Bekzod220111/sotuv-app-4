from django.contrib import admin
from .models import Product, Category, ProductInput

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductInput)

admin.site.register(Category)
