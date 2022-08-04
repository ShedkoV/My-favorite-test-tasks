from rest_framework import serializers
from .models import Book, Customer, BoughtBook


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BoughtBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BoughtBook
        fields = '__all__'
