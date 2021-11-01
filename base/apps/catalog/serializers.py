from rest_framework import serializers
from .models import Brand
from .models import Product


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def get_image(self, car):
        request = self.context.get('request')
        image = car.photo.url
        return request.build_absolute_uri(image)
