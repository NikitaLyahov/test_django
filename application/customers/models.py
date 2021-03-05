from django.db import models

from application.models import AbstractBaseModel


class Customers(AbstractBaseModel):
    first_name = models.TextField()
    last_name = models.TextField()

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'Customer {self.id} - {self.full_name}'

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'


class Emails(AbstractBaseModel):
    address = models.TextField()
    customer = models.ForeignKey(Customers,
                                 related_name='emails',
                                 on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Customer {self.customer.full_name} - {self.address}'

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'
