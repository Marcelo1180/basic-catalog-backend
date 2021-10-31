from django.contrib import admin
from .models import Brand
from .models import Product
from .models import ProductCounter
from .models import ProductTracker

"""
Brand
"""
admin.site.register(Brand)

"""
Product
"""
admin.site.register(Product)
admin.site.register(ProductCounter)
admin.site.register(ProductTracker)
