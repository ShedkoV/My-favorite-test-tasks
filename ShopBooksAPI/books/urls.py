from django.urls import path
from .views import BookListView, BookDetailView, CustomerListView, CustomerDetailView, BoughtBookAPIView


urlpatterns = [
    path('api/books', BookListView.as_view()),
    path('api/customers', CustomerListView.as_view()),
    path('api/buybook', BoughtBookAPIView.as_view()),
    path('api/returnbook', BoughtBookAPIView.as_view()),
    path('api/customers/<int:pk>/', CustomerDetailView.as_view()),
    path('api/books/<int:pk>/', BookDetailView.as_view()),
]
