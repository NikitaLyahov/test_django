from django.db import models

from application.models import AbstractBaseModel


class AbstractProductsModel(AbstractBaseModel):
    class Price(models.IntegerChoices):
        SIX = 6
        TWO = 2

    name = models.TextField()
    price = models.IntegerField(choices=Price.choices)

    def __str__(self) -> str:
        return f'{self.name} ({self.price})'

    class Meta:
        abstract = True


class Products(AbstractProductsModel):
    class Meta:
        db_table = 'customer_products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class NonCustomerProducts(AbstractProductsModel):
    class Meta:
        db_table = 'non_customer_products'
        verbose_name = 'Non Customer Product'
        verbose_name_plural = 'Non Customer Products'
