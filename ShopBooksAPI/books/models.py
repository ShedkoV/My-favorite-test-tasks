from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=125)
    bonuses = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=125)
    price = models.FloatField()

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.name


class BoughtBook(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=False)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'bough_books'
