from rest_framework.generics import \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import BookSerializers, CustomerSerializers, BoughtBookSerializers
from .models import Book, Customer


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class CustomerListView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class BoughtBookAPIView(CreateAPIView):
    serializer_class = BoughtBookSerializers

    def perform_create(self, serializer):
        book = Book.objects.get(
            pk=serializer.data.get('book')
        )
        
        customer = Customer.objects.get(
            pk=serializer.data.get('customer')
        )

        if customer.bonuses >= 100:
            customer.bonuses = 0
        elif book.price > 9.99: 
            customer.bonuses += 20
        else:
            customer.bonuses += 10
            
        customer.save()
