from django.contrib import admin

from products.models import (
    Products,
    NonCustomerProducts,
)


admin.site.register(Products)
admin.site.register(NonCustomerProducts)
