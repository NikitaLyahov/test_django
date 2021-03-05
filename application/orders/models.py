from django.db import models

from application.models import AbstractBaseModel
from orders.managers import OrdersManager
from customers.models import Customers
from products.models import (
    Products,
    NonCustomerProducts,
)


class Orders(AbstractBaseModel):
    number = models.TextField()
    customer = models.ForeignKey(Customers,
                                 related_name='orders',
                                 on_delete=models.CASCADE)

    objects = OrdersManager()

    def __str__(self) -> str:
        return f'Order {self.id} ({self.number}) - {self.customer.full_name}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class Status(AbstractBaseModel):
    paid = models.BooleanField(default=False)
    order = models.OneToOneField(Orders,
                                 related_name='status',
                                 on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Status {self.paid} - order {self.order.id}'

    class Meta:
        db_table = 'order_status'
        verbose_name = 'status'
        verbose_name_plural = 'statuses'


class Items(AbstractBaseModel):
    order = models.ForeignKey(Orders,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Products,
                                null=True,
                                related_name='items',
                                on_delete=models.DO_NOTHING)
    non_customer_product = models.ForeignKey(NonCustomerProducts,
                                             null=True,
                                             related_name='items',
                                             on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'Item {self.id} - order {self.order.id}'

    class Meta:
        db_table = 'order_items'
        verbose_name = 'item'
        verbose_name_plural = 'items'
