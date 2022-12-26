from rest_framework import serializers

from .models import *


# class ProductSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"
#
#
# class FirmaSerializers(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=99)
#     address = serializers.CharField(max_length=222)
#
#     class Meta:
#         model = Firma
#         fields = "__all__"
#
#     def create(self, validated_data):
#         massage = Firma.objects.create(
#             name=validated_data['name'],
#             address=validated_data['address']
#         )
#         return massage
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data['name']
#         instance.address = validated_data['address']
#         return instance


# class FirmaSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Firma
#         fields = "__all__"
#
#
# class CategorySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"


class FirmaSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=99)
    address = serializers.CharField(max_length=222)

    def create(self, validated_data):
        massage = Firma.objects.create(
            name=validated_data['name'],
            address=validated_data['address'],
        )
        return massage

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        return instance


class CategorySerializers(serializers.Serializer):
    category_name = serializers.CharField(max_length=99)

    def create(self, validated_data):
        massage = Category.objects.create(
            category_name=validated_data['category_name']
        )
        return massage

    def update(self, instance, validated_data):
        instance.category_name = validated_data['category_name']
        return instance


class ProductSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=99)
    product_sum = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        massage = Product.objects.create(
            name=validated_data['name'],
            product_sum=validated_data['product_sum'],
            firm_id=validated_data['firm_id'],
            category_id=validated_data['category_id'],
        )
        return massage

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.product_sum = validated_data['product_sum']
        instance.firm = validated_data['firm']
        instance.category = validated_data['category']
        return instance
