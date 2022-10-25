from rest_framework import serializers
from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Stock,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
        )


class ProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField(write_only=True)
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'category_id',
            'brand',
            'brand_id',
            'stock',
        )
        read_only_fields = ('stock',)


class BrandProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'products',
        )


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone',
            'address',
        )
    

class StockSerializer(serializers.ModelSerializer):
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField(write_only=True)
    product= serializers.StringRelatedField()
    product_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Stock
        fields = (
            'id',
            'user',
            'firm',
            'firm_id',
            'transaction',
            'product',
            'product_id',
            'quantitiy',
            'price',
            'price_total',
        )
        read_only_fields = ('price_total',)

    def validate(self, data):
        """
        Check if the quantity mor then product stock.
        """
        if data['transaction'] == 'O':
            product = Product.objects.get(id=data['product_id'])
            if data.get('quantitiy') > product.stock:
                raise serializers.ValidationError(f"Do not have enough stock! Current stock is {product.stock}")
        return data